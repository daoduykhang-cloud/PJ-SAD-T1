import sqlite3
import os
import json
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory, session

# Khởi tạo ứng dụng Flask
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "restaurant.db")

app = Flask(__name__, template_folder=BASE_DIR, static_folder=BASE_DIR)
app.secret_key = 'ant_bistro_super_secret_key_2026'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS areas (
        area_id TEXT PRIMARY KEY,
        area_name TEXT NOT NULL,
        floor INTEGER DEFAULT 1,
        description TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tables (
        table_id TEXT PRIMARY KEY,
        area_id TEXT NOT NULL,
        capacity INTEGER NOT NULL,
        shape TEXT DEFAULT 'square',
        status TEXT DEFAULT 'Available',
        description TEXT,
        FOREIGN KEY (area_id) REFERENCES areas(area_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id TEXT PRIMARY KEY,
        full_name TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        email TEXT,
        is_vip INTEGER DEFAULT 0
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        account_id TEXT PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'customer',
        full_name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        reservation_id TEXT PRIMARY KEY,
        customer_id TEXT NOT NULL,
        customer_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        table_id TEXT NOT NULL,
        area_id TEXT NOT NULL,
        booking_date TEXT NOT NULL,
        time_slot TEXT NOT NULL,
        party_size INTEGER NOT NULL,
        status TEXT DEFAULT 'Confirmed',
        qr_token TEXT NOT NULL,
        special_note TEXT,
        checkin_time TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (table_id) REFERENCES tables(table_id),
        FOREIGN KEY (area_id) REFERENCES areas(area_id)
    );
    """)

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM areas;")
    if cursor.fetchone()[0] == 0:
        seed_sample_data(conn)

    conn.close()

def seed_sample_data(conn):
    cursor = conn.cursor()

    areas_data = [
        ('A01', 'Sushi Bar & Sảnh Chính', 1, 'Không gian ấm cúng, xem trực tiếp đầu bếp làm Sushi'),
        ('A02', 'Khu Sân Vườn Zen Garden', 1, 'Hồ cá Koi, cây xanh phong cách Nhật Bản thanh tịnh'),
        ('A03', 'Phòng VIP Samurai Riêng Tư', 2, 'Phòng riêng sang trọng, chiếu Tatami, cách âm cao cấp'),
        ('A04', 'Sân Thượng Skyview Lounge', 3, 'Ngắm toàn cảnh thành phố về đêm, gió mát lãng mạn')
    ]
    cursor.executemany("INSERT INTO areas (area_id, area_name, floor, description) VALUES (?, ?, ?, ?);", areas_data)

    tables_data = [

        ('T101', 'A01', 4, 'square', 'Reserved', 'Bàn view quầy Sushi Bar'),
        ('T102', 'A01', 4, 'square', 'Available', 'Bàn tiêu chuẩn gần lối đi'),
        ('T103', 'A01', 6, 'rect', 'Occupied', 'Bàn sofa gia đình êm ái'),
        ('T104', 'A01', 2, 'round', 'Available', 'Bàn đôi hẹn hò ấm cúng'),
        ('T105', 'A01', 4, 'square', 'Available', 'Bàn tiêu chuẩn trung tâm'),
        ('T106', 'A01', 8, 'rect', 'Reserved', 'Bàn dài nhóm bạn liên hoan'),
        ('T107', 'A01', 2, 'round', 'Available', 'Bàn đôi góc yên tĩnh'),
        ('T108', 'A01', 4, 'square', 'Cleaning', 'Đang dọn dẹp vệ sinh'),

        ('G201', 'A02', 4, 'round', 'Available', 'Bàn tròn dưới tán phong đỏ'),
        ('G202', 'A02', 4, 'round', 'Available', 'Bàn cạnh đài nước đá Zen'),
        ('G203', 'A02', 6, 'rect', 'Reserved', 'Bàn dài view hồ cá Koi'),
        ('G204', 'A02', 4, 'round', 'Available', 'Bàn tròn ngoài trời thoáng mát'),
        ('G205', 'A02', 8, 'rect', 'Occupied', 'Bàn tiệc nướng BBQ sân vườn'),
        ('G206', 'A02', 2, 'round', 'Available', 'Bàn đôi ngắm hoa anh đào'),

        ('VIP01', 'A03', 8, 'rect', 'Reserved', 'Phòng VIP Hoàng Gia, tranh thủy mặc'),
        ('VIP02', 'A03', 12, 'rect', 'Available', 'Phòng VIP Yến Tiệc tiếp khách lớn'),
        ('VIP03', 'A03', 6, 'round', 'Available', 'Phòng VIP Chiếu Tatami ấm cúng'),
        ('VIP04', 'A03', 10, 'rect', 'Maintenance', 'Đang bảo trì điều hòa'),

        ('RT301', 'A04', 4, 'square', 'Available', 'Bàn kính ngắm hoàng hôn'),
        ('RT302', 'A04', 2, 'round', 'Occupied', 'Bàn nến lãng mạn cạnh ban công'),
        ('RT303', 'A04', 4, 'square', 'Reserved', 'Bàn gần quầy Cocktail ngoài trời'),
        ('RT304', 'A04', 6, 'rect', 'Available', 'Bàn sofa chill ngắm sao đêm'),
        ('RT305', 'A04', 4, 'square', 'Available', 'Bàn gió lộng tự nhiên'),
        ('RT306', 'A04', 8, 'rect', 'Available', 'Bàn tiệc ngắm view thành phố')
    ]
    cursor.executemany("INSERT INTO tables (table_id, area_id, capacity, shape, status, description) VALUES (?, ?, ?, ?, ?, ?);", tables_data)

    customers_data = [
        ('CUS-001', 'Nguyễn Văn An', '0912345678', 'an.nguyen@example.com', 1),
        ('CUS-002', 'Lê Thu Trang', '0987654321', 'trang.le@example.com', 0),
        ('CUS-003', 'Trần Minh Hoàng', '0903112233', 'hoang.tran@example.com', 0),
        ('CUS-004', 'Phạm Đức Anh', '0934556677', 'anh.pham@example.com', 1),
        ('CUS-005', 'Vũ Hải Đăng', '0948998877', 'dang.vu@example.com', 0)
    ]
    cursor.executemany("INSERT INTO customers (customer_id, full_name, phone, email, is_vip) VALUES (?, ?, ?, ?, ?);", customers_data)

    accounts_data = [
        ('ACC-001', 'admin', 'admin123', 'manager', 'Quản Lý Ant Bistro', 'admin@antbistro.vn', '0900000001'),
        ('ACC-002', 'letan01', '123456', 'staff', 'Lễ Tân Mai Anh', 'letan@antbistro.vn', '0900000002'),
        ('ACC-003', 'khachhang1', '123456', 'customer', 'Nguyễn Văn An', 'an.nguyen@example.com', '0912345678'),
        ('ACC-004', 'khachhang2', '123456', 'customer', 'Lê Thu Trang', 'trang.le@example.com', '0987654321')
    ]
    cursor.executemany("""
    INSERT INTO accounts (account_id, username, password, role, full_name, email, phone)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """, accounts_data)

    today = datetime.now().strftime('%Y-%m-%d')
    rsv_data = [
        ('RSV-001', 'CUS-001', 'Nguyễn Văn An', '0912345678', 'T101', 'A01', today, '19:00', 4, 'Confirmed', 'RSV-001|T101|0912345678|19:00', 'Tiệc sinh nhật, yêu cầu hoa tươi và nến.', None),
        ('RSV-002', 'CUS-002', 'Lê Thu Trang', '0987654321', 'T106', 'A01', today, '18:30', 8, 'Confirmed', 'RSV-002|T106|0987654321|18:30', 'Gặp gỡ gia đình, có trẻ nhỏ cần ghế phụ.', None),
        ('RSV-003', 'CUS-003', 'Trần Minh Hoàng', '0903112233', 'G203', 'A02', today, '19:30', 6, 'Confirmed', 'RSV-003|G203|0903112233|19:30', 'Bàn ngoài trời thoáng gió view hồ Koi.', None),
        ('RSV-004', 'CUS-004', 'Phạm Đức Anh', '0934556677', 'VIP01', 'A03', today, '19:00', 8, 'Confirmed', 'RSV-004|VIP01|0934556677|19:00', 'Tiếp đón khách hàng đối tác quan trọng.', None),
        ('RSV-005', 'CUS-005', 'Vũ Hải Đăng', '0948998877', 'RT303', 'A04', today, '20:00', 4, 'Confirmed', 'RSV-005|RT303|0948998877|20:00', 'Kỷ niệm ngày cưới, view đèn thành phố.', None)
    ]
    cursor.executemany("""
    INSERT INTO reservations 
    (reservation_id, customer_id, customer_name, phone, table_id, area_id, booking_date, time_slot, party_size, status, qr_token, special_note, checkin_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, rsv_data)

    conn.commit()

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'Restaurant_system.html')

@app.route('/api/auth/login', methods=['POST'])
def auth_login():
    data = request.json or {}
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    if not username or not password:
        return jsonify({"success": False, "message": "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu!"}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username = ? AND password = ?;", (username, password))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"success": False, "message": "Tên đăng nhập hoặc mật khẩu không chính xác!"}), 401

    user_info = {
        "accountId": user['account_id'],
        "username": user['username'],
        "role": user['role'],
        "fullName": user['full_name'],
        "email": user['email'],
        "phone": user['phone']
    }

    session['user'] = user_info

    return jsonify({
        "success": True,
        "message": f"Chào mừng {user['full_name']} quay trở lại!",
        "user": user_info
    })

@app.route('/api/auth/register', methods=['POST'])
def auth_register():
    data = request.json or {}
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    full_name = data.get('fullName', '').strip()
    phone = data.get('phone', '').strip()
    email = data.get('email', '').strip()

    if not username or not password or not full_name or not phone:
        return jsonify({"success": False, "message": "Vui lòng điền đầy đủ họ tên, SĐT, username và mật khẩu!"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT account_id FROM accounts WHERE username = ?;", (username,))
    if cursor.fetchone():
        conn.close()
        return jsonify({"success": False, "message": "Tên đăng nhập này đã được sử dụng. Vui lòng chọn tên khác!"}), 400

    cursor.execute("SELECT account_id FROM accounts WHERE phone = ?;", (phone,))
    if cursor.fetchone():
        conn.close()
        return jsonify({"success": False, "message": "Số điện thoại này đã được đăng ký tài khoản!"}), 400

    cursor.execute("SELECT COUNT(*) FROM accounts;")
    acc_count = cursor.fetchone()[0] + 1
    account_id = f"ACC-{str(acc_count).zfill(3)}"

    cursor.execute("SELECT COUNT(*) FROM customers;")
    cus_count = cursor.fetchone()[0] + 1
    customer_id = f"CUS-{str(cus_count).zfill(3)}"

    cursor.execute("""
    INSERT INTO accounts (account_id, username, password, role, full_name, email, phone)
    VALUES (?, ?, ?, 'customer', ?, ?, ?);
    """, (account_id, username, password, full_name, email, phone))

    cursor.execute("""
    INSERT OR REPLACE INTO customers (customer_id, full_name, phone, email, is_vip)
    VALUES (?, ?, ?, ?, 0);
    """, (customer_id, full_name, phone, email))

    conn.commit()
    conn.close()

    user_info = {
        "accountId": account_id,
        "username": username,
        "role": "customer",
        "fullName": full_name,
        "email": email,
        "phone": phone
    }

    session['user'] = user_info

    return jsonify({
        "success": True,
        "message": "Đăng ký tài khoản thành công!",
        "user": user_info
    })

@app.route('/api/auth/logout', methods=['POST'])
def auth_logout():
    session.pop('user', None)
    return jsonify({"success": True, "message": "Đã đăng xuất tài khoản thành công!"})

@app.route('/api/auth/me', methods=['GET'])
def auth_me():
    user = session.get('user')
    if user:
        return jsonify({"authenticated": True, "user": user})
    return jsonify({"authenticated": False, "user": None})

@app.route('/api/areas', methods=['GET'])
def get_areas():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT area_id as areaId, area_name as areaName, floor, description as desc FROM areas;")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(rows)

@app.route('/api/tables', methods=['GET'])
def get_tables():
    area_id = request.args.get('area_id')
    status = request.args.get('status')
    
    conn = get_db()
    cursor = conn.cursor()
    query = "SELECT table_id as tableId, area_id as areaId, capacity, shape, status, description as desc FROM tables WHERE 1=1"
    params = []
    
    if area_id and area_id != 'ALL':
        query += " AND area_id = ?"
        params.append(area_id)
    if status and status != 'ALL':
        query += " AND status = ?"
        params.append(status)
        
    cursor.execute(query, params)
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(rows)

@app.route('/api/check-availability', methods=['POST'])
def check_availability():
    data = request.json or {}
    date = data.get('date')
    time = data.get('time')
    guests = int(data.get('guests', 2))
    area_id = data.get('area_id', 'ALL')

    conn = get_db()
    cursor = conn.cursor()

    query = """
    SELECT t.table_id as tableId, t.area_id as areaId, t.capacity, t.shape, t.status, t.description as desc,
           a.area_name as areaName
    FROM tables t
    JOIN areas a ON t.area_id = a.area_id
    WHERE t.status != 'Maintenance' AND t.capacity >= ?
    """
    params = [guests]

    if area_id and area_id != 'ALL':
        query += " AND t.area_id = ?"
        params.append(area_id)

    cursor.execute(query, params)
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return jsonify({
        "success": True,
        "availableCount": len([r for r in rows if r['status'] == 'Available']),
        "tables": rows
    })

@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    data = request.json or {}
    full_name = data.get('fullName', '').strip()
    phone = data.get('phone', '').strip()
    email = data.get('email', '').strip()
    date = data.get('date')
    time = data.get('time')
    guests = int(data.get('guests', 2))
    table_id = data.get('tableId', '').strip()
    note = data.get('note', '')

    if not full_name or not phone or not table_id:
        return jsonify({"success": False, "message": "Vui lòng nhập đầy đủ họ tên, SĐT và bàn cần đặt!"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT status, area_id, capacity FROM tables WHERE table_id = ?;", (table_id,))
    table_row = cursor.fetchone()
    if not table_row:
        conn.close()
        return jsonify({"success": False, "message": "Bàn không tồn tại!"}), 404

    if table_row['status'] != 'Available':
        conn.close()
        return jsonify({"success": False, "message": f"Bàn {table_id} hiện không còn trống!"}), 400

    cursor.execute("SELECT customer_id FROM customers WHERE phone = ?;", (phone,))
    cus_row = cursor.fetchone()
    if cus_row:
        customer_id = cus_row['customer_id']
    else:
        cursor.execute("SELECT COUNT(*) FROM customers;")
        count_c = cursor.fetchone()[0] + 1
        customer_id = f"CUS-{str(count_c).zfill(3)}"
        cursor.execute("INSERT INTO customers (customer_id, full_name, phone, email, is_vip) VALUES (?, ?, ?, ?, ?);",
                       (customer_id, full_name, phone, email, 0))

    cursor.execute("SELECT COUNT(*) FROM reservations;")
    count_r = cursor.fetchone()[0] + 1
    reservation_id = f"RSV-{str(count_r).zfill(3)}"
    qr_token = f"{reservation_id}|{table_id}|{phone}|{time}"

    cursor.execute("""
    INSERT INTO reservations 
    (reservation_id, customer_id, customer_name, phone, table_id, area_id, booking_date, time_slot, party_size, status, qr_token, special_note)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Confirmed', ?, ?);
    """, (reservation_id, customer_id, full_name, phone, table_id, table_row['area_id'], date, time, guests, qr_token, note))

    cursor.execute("UPDATE tables SET status = 'Reserved' WHERE table_id = ?;", (table_id,))

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": f"Đặt bàn thành công cho {full_name}!",
        "reservation": {
            "reservationId": reservation_id,
            "customerName": full_name,
            "phone": phone,
            "tableId": table_id,
            "areaId": table_row['area_id'],
            "bookingDate": date,
            "timeSlot": time,
            "partySize": guests,
            "status": "Confirmed",
            "qrToken": qr_token,
            "specialNote": note
        }
    })

@app.route('/api/reservations', methods=['GET'])
def get_reservations():
    search = request.args.get('search', '').strip().lower()
    status = request.args.get('status', 'ALL')

    conn = get_db()
    cursor = conn.cursor()
    query = """
    SELECT reservation_id as reservationId, customer_id as customerId, customer_name as customerName,
           phone, table_id as tableId, area_id as areaId, booking_date as bookingDate,
           time_slot as timeSlot, party_size as partySize, status, qr_token as qrToken,
           special_note as specialNote, checkin_time as checkInTime
    FROM reservations
    WHERE 1=1
    """
    params = []

    if status and status != 'ALL':
        query += " AND status = ?"
        params.append(status)

    if search:
        query += " AND (LOWER(reservation_id) LIKE ? OR LOWER(customer_name) LIKE ? OR phone LIKE ? OR LOWER(table_id) LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term, term, term])

    query += " ORDER BY booking_date DESC, time_slot ASC;"
    cursor.execute(query, params)
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return jsonify(rows)

@app.route('/api/check-in', methods=['POST'])
def handle_checkin():
    data = request.json or {}
    code = data.get('code', '').strip().upper()

    if not code:
        return jsonify({"success": False, "message": "Vui lòng cung cấp mã QR hoặc mã đặt bàn!"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM reservations 
    WHERE reservation_id = ? OR qr_token LIKE ? OR phone = ?;
    """, (code, f"%{code}%", code))
    rsv = cursor.fetchone()

    if not rsv:
        conn.close()
        return jsonify({"success": False, "message": f"Không tìm thấy lịch đặt bàn nào với mã: {code}!"}), 404

    if rsv['status'] == 'CheckedIn':
        conn.close()
        return jsonify({
            "success": True,
            "alreadyCheckedIn": True,
            "message": f"Khách hàng {rsv['customer_name']} đã check-in vào lúc {rsv['checkin_time']}.",
            "reservation": dict(rsv)
        })

    if rsv['status'] == 'Cancelled':
        conn.close()
        return jsonify({"success": False, "message": f"Lịch đặt bàn {rsv['reservation_id']} đã bị HỦY trước đó!"}), 400

    now_str = datetime.now().strftime('%H:%M Hôm nay')
    cursor.execute("UPDATE reservations SET status = 'CheckedIn', checkin_time = ? WHERE reservation_id = ?;",
                   (now_str, rsv['reservation_id']))

    cursor.execute("UPDATE tables SET status = 'Occupied' WHERE table_id = ?;", (rsv['table_id'],))

    conn.commit()

    cursor.execute("SELECT * FROM reservations WHERE reservation_id = ?;", (rsv['reservation_id'],))
    updated_rsv = dict(cursor.fetchone())
    conn.close()

    return jsonify({
        "success": True,
        "message": f"Check-in thành công cho khách hàng {updated_rsv['customer_name']} tại bàn {updated_rsv['table_id']}!",
        "reservation": updated_rsv
    })

@app.route('/api/reservations/<rsv_id>', methods=['PUT'])
def modify_reservation(rsv_id):
    data = request.json or {}
    new_table_id = data.get('tableId')
    new_date = data.get('date')
    new_time = data.get('time')
    new_guests = int(data.get('guests', 2))

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reservations WHERE reservation_id = ?;", (rsv_id,))
    rsv = cursor.fetchone()
    if not rsv:
        conn.close()
        return jsonify({"success": False, "message": "Không tìm thấy lượt đặt bàn!"}), 404

    old_table_id = rsv['table_id']

    if new_table_id and new_table_id != old_table_id:
        cursor.execute("SELECT status, area_id FROM tables WHERE table_id = ?;", (new_table_id,))
        new_tbl = cursor.fetchone()
        if not new_tbl or new_tbl['status'] != 'Available':
            conn.close()
            return jsonify({"success": False, "message": f"Bàn {new_table_id} không còn trống để đổi!"}), 400

        cursor.execute("UPDATE tables SET status = 'Available' WHERE table_id = ?;", (old_table_id,))
        cursor.execute("UPDATE tables SET status = 'Reserved' WHERE table_id = ?;", (new_table_id,))
        new_area_id = new_tbl['area_id']
    else:
        new_table_id = old_table_id
        new_area_id = rsv['area_id']

    new_qr = f"{rsv_id}|{new_table_id}|{rsv['phone']}|{new_time}"
    cursor.execute("""
    UPDATE reservations 
    SET table_id = ?, area_id = ?, booking_date = ?, time_slot = ?, party_size = ?, qr_token = ?
    WHERE reservation_id = ?;
    """, (new_table_id, new_area_id, new_date, new_time, new_guests, new_qr, rsv_id))

    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": f"Đổi sang bàn {new_table_id} thành công!"})

@app.route('/api/reservations/<rsv_id>/cancel', methods=['POST'])
def cancel_reservation(rsv_id):
    data = request.json or {}
    reason = data.get('reason', 'Khách yêu cầu hủy')

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reservations WHERE reservation_id = ?;", (rsv_id,))
    rsv = cursor.fetchone()
    if not rsv:
        conn.close()
        return jsonify({"success": False, "message": "Không tìm thấy lượt đặt bàn!"}), 404

    note = (rsv['special_note'] or '') + f" [Lý do hủy: {reason}]"
    cursor.execute("UPDATE reservations SET status = 'Cancelled', special_note = ? WHERE reservation_id = ?;", (note, rsv_id))
    cursor.execute("UPDATE tables SET status = 'Available' WHERE table_id = ?;", (rsv['table_id'],))

    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": f"Đã hủy đặt bàn {rsv_id} và hoàn trả bàn {rsv['table_id']} về trạng thái Trống."})

@app.route('/api/tables/<table_id>/release', methods=['POST'])
def release_table(table_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE reservations SET status = 'Completed' WHERE table_id = ? AND status = 'CheckedIn';", (table_id,))
    cursor.execute("UPDATE tables SET status = 'Cleaning' WHERE table_id = ?;", (table_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": f"Đã trả bàn {table_id}. Bàn chuyển sang Chờ Dọn Dẹp (Cleaning)."})

@app.route('/api/tables/<table_id>/ready', methods=['POST'])
def table_ready(table_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tables SET status = 'Available' WHERE table_id = ?;", (table_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": f"Bàn {table_id} đã sẵn sàng đón khách mới!"})

@app.route('/api/tables', methods=['POST'])
def add_or_update_table():
    data = request.json or {}
    table_id = data.get('tableId', '').strip().upper()
    area_id = data.get('areaId')
    capacity = int(data.get('capacity', 4))
    shape = data.get('shape', 'square')
    status = data.get('status', 'Available')
    desc = data.get('desc', '')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO tables (table_id, area_id, capacity, shape, status, description)
    VALUES (?, ?, ?, ?, ?, ?)
    ON CONFLICT(table_id) DO UPDATE SET
        area_id = excluded.area_id,
        capacity = excluded.capacity,
        shape = excluded.shape,
        status = excluded.status,
        description = excluded.description;
    """, (table_id, area_id, capacity, shape, status, desc))
    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": f"Đã lưu bàn {table_id} vào cơ sở dữ liệu!"})

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tables;")
    total_tables = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tables WHERE status = 'Available';")
    avail_tables = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tables WHERE status = 'Reserved';")
    reserved_tables = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tables WHERE status = 'Occupied';")
    occupied_tables = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reservations WHERE status != 'Cancelled';")
    total_bookings = cursor.fetchone()[0]

    occupancy_rate = round(((reserved_tables + occupied_tables) / total_tables * 100), 1) if total_tables > 0 else 0

    conn.close()

    return jsonify({
        "totalTables": total_tables,
        "availableTables": avail_tables,
        "reservedTables": reserved_tables,
        "occupiedTables": occupied_tables,
        "totalBookings": total_bookings,
        "occupancyRate": occupancy_rate
    })


@app.route('/api/reset-data', methods=['POST'])
def reset_data():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS reservations;")
    cursor.execute("DROP TABLE IF EXISTS accounts;")
    cursor.execute("DROP TABLE IF EXISTS customers;")
    cursor.execute("DROP TABLE IF EXISTS tables;")
    cursor.execute("DROP TABLE IF EXISTS areas;")
    conn.commit()
    conn.close()

    init_db()
    return jsonify({"success": True, "message": "Đã khôi phục toàn bộ CSDL mẫu ban đầu của Ant Bistro!"})


if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    init_db()
    print("=" * 60)
    print("ANT BISTRO - HE THONG DAT BAN & QUAN LY NHA HANG (FLASK BACKEND)")
    print("CSDL SQLite:", DB_PATH)
    print("Truy cap ung dung tai: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)

