# 🍽️ Restaurant Table Reservation System

**Topic 1: Khảo sát hiện trạng, xác định bài toán và lựa chọn quy trình phát triển**


## 1. Tổng quan và phạm vi

### 1.1. Bài toán

Hệ thống hỗ trợ khách hàng và nhân viên nhà hàng quản lý việc đặt bàn, kiểm tra tình trạng bàn, bố trí bàn và check-in.

Các nghiệp vụ chính:

- Tra cứu bàn.
- Kiểm tra bàn khả dụng.
- Đặt, đổi và hủy đặt bàn.
- Bố trí bàn.
- Check-in.
- Cập nhật trạng thái bàn.
- Quản lý thông tin khách hàng.

### 1.2. Hiện trạng

Việc đặt bàn có thể được thực hiện thủ công, gây khó khăn trong việc kiểm tra bàn trống và nguy cơ xảy ra trùng lịch.

**Giả định:** Hệ thống được xây dựng cho một nhà hàng.

### 1.3. Đối tượng sử dụng

| Đối tượng | Chức năng |
|---|---|
| **Khách hàng** | Tra cứu, kiểm tra khả dụng, đặt, đổi, hủy bàn |
| **Nhân viên** | Đặt hộ, bố trí bàn, check-in, cập nhật trạng thái và quản lý khách |
| **Quản trị viên** | Quản lý bàn, khu vực và các chức năng của nhân viên |

### 1.4. Phạm vi

**Trong phạm vi:**

Tra cứu bàn, kiểm tra khả dụng, đặt / xác nhận, đổi, hủy, bố trí bàn, check-in, cập nhật trạng thái bàn và quản lý khách.

**Ngoài phạm vi:**

Đặt món, thanh toán, khuyến mãi, tích điểm và quản lý nhiều chi nhánh.


## 2. Input → Processing → Output

### Input

| Nhóm | Dữ liệu |
|---|---|
| Khách hàng | Họ tên, số điện thoại, email |
| Đặt bàn | Ngày, giờ bắt đầu, giờ kết thúc, số người, khu vực, bàn mong muốn, ghi chú |
| Bàn | Mã bàn, sức chứa, khu vực, trạng thái |
| Vận hành | Mã đặt bàn, yêu cầu đổi / hủy, thông tin check-in |

### Processing

```text
Nhập thời gian + số người
        ↓
Kiểm tra bàn khả dụng
        ↓
Chọn bàn + nhập thông tin khách
        ↓
Kiểm tra hợp lệ
        ↓
Tạo và xác nhận đặt bàn
        ↓
Check-in
        ↓
Hoàn tất lượt sử dụng
```

### Output

- Danh sách bàn khả dụng.
- Thông tin bàn.
- Mã và thông tin đặt bàn.
- Kết quả đặt / đổi / hủy.
- Trạng thái đặt bàn và bàn.
- Thông tin check-in.


## 3. Business Rules

| ID | Quy tắc nghiệp vụ |
|---|---|
| **BR-01** | Một bàn không được có hai đặt bàn hiệu lực chồng thời gian. |
| **BR-02** | Số người không được vượt quá sức chứa của bàn. |
| **BR-03** | Chỉ bàn khả dụng mới được đặt. |
| **BR-04** | Họ tên, số điện thoại, thời gian và số người là thông tin bắt buộc. |
| **BR-05** | Mỗi đặt bàn có một mã duy nhất. |
| **BR-06** | Chỉ đặt bàn còn hiệu lực mới được đổi hoặc hủy. |
| **BR-07** | Khi đổi thời gian hoặc bàn phải kiểm tra lại khả dụng. |
| **BR-08** | Chỉ đặt bàn hợp lệ mới được check-in. |
| **BR-09** | Khi check-in, hệ thống cập nhật trạng thái đặt bàn và bàn. |
| **BR-10** | Hệ thống phải ngăn việc hai người cùng đặt một bàn trong cùng thời gian. |

### Trạng thái đặt bàn

```text
Confirmed → Checked-in → Completed
     └──────────────→ Cancelled
```

### Trạng thái bàn

```text
Available ↔ Occupied
Available ↔ Unavailable
```


## 4. Yêu cầu hệ thống (SRS)

### 4.1. Yêu cầu chức năng

| ID | Yêu cầu | Đối tượng |
|---|---|---|
| **FR-01** | Tra cứu bàn theo khu vực, sức chứa và trạng thái | Khách hàng, Nhân viên |
| **FR-02** | Kiểm tra bàn khả dụng theo thời gian và số người | Khách hàng, Nhân viên |
| **FR-03** | Tạo và xác nhận đặt bàn, sinh mã đặt bàn | Khách hàng, Nhân viên |
| **FR-04** | Ngăn đặt trùng lịch | Hệ thống |
| **FR-05** | Đổi thông tin hoặc đổi bàn | Khách hàng, Nhân viên |
| **FR-06** | Hủy đặt bàn | Khách hàng, Nhân viên |
| **FR-07** | Bố trí hoặc thay đổi bàn | Nhân viên, Quản trị viên |
| **FR-08** | Check-in đặt bàn | Nhân viên |
| **FR-09** | Cập nhật trạng thái bàn | Nhân viên, Quản trị viên |
| **FR-10** | Quản lý thông tin khách hàng | Nhân viên, Quản trị viên |
| **FR-11** | Thông báo kết quả thao tác | Hệ thống |
| **FR-12** | Quản lý bàn và khu vực | Quản trị viên |

### 4.2. Yêu cầu phi chức năng

| ID | Yêu cầu |
|---|---|
| **NFR-01** | Không xảy ra đặt trùng bàn khi nhiều yêu cầu được xử lý đồng thời. |
| **NFR-02** | Chức năng của nhân viên và quản trị viên phải được xác thực và phân quyền. |
| **NFR-03** | Thông tin cá nhân của khách hàng phải được bảo vệ. |
| **NFR-04** | Dữ liệu đặt bàn và trạng thái bàn phải đảm bảo tính nhất quán. |


## 5. Giả định

- Hệ thống áp dụng cho một nhà hàng.
- Mỗi đặt bàn gắn với một bàn.
- Mỗi đặt bàn có thời gian bắt đầu và kết thúc.
- Đặt bàn hợp lệ được xác nhận ngay.
- Khách hàng có thể tự đặt hoặc nhân viên đặt hộ.
- Check-in do nhân viên thực hiện.
- Khách hàng sử dụng mã đặt bàn và số điện thoại để đổi hoặc hủy đặt bàn.


## 6. Quy trình phát triển

### Lựa chọn: Scrum

| Quy trình | Đánh giá |
|---|---|
| Waterfall | Không phù hợp vì yêu cầu có thể thay đổi trong quá trình phát triển. |
| Agile | Phù hợp với yêu cầu cần phản hồi và điều chỉnh. |
| **Scrum** | **Phù hợp nhất** vì phát triển theo Sprint và có phản hồi thường xuyên. |
| Spiral | Tương đối phức tạp với quy mô hệ thống. |

### Lý do chọn Scrum

- Phát triển hệ thống theo từng giai đoạn.
- Dễ tiếp nhận phản hồi và thay đổi yêu cầu.
- Có thể ưu tiên các chức năng quan trọng trước.
- Phù hợp với project có quy mô vừa và nhỏ.

## 7. Deliverables

Các sản phẩm được xây dựng dựa trên tài liệu đặc tả này:

| # | Deliverable |
|---|---|
| 1 | Business Rules |
| 2 | SRS |
| 3 | Use Case Diagram |
| 4 | Activity Diagram |
| 5 | Class Diagram / ERD |
| 6 | Sequence Diagram |
| 7 | UI Prototype |
