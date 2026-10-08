# 🍽️ Restaurant Table Reservation System

**Topic 1: Khảo sát hiện trạng, xác định bài toán và lựa chọn quy trình phát triển**

> Tài liệu đặc tả yêu cầu ban đầu cho hệ thống đặt bàn nhà hàng.  
> Không bao gồm source code, database hoặc thiết kế chi tiết.

### Quy ước

| Nhãn | Ý nghĩa |
|---|---|
| **[Đề bài]** | Thông tin từ đề bài |
| **[GĐ]** | Giả định cần xác nhận |
| **[ĐX]** | Đề xuất của nhóm |
| **OQ** | Câu hỏi mở |

---

# 1. Tổng quan và phạm vi

## 1.1. Bài toán

**[Đề bài]** Hệ thống hỗ trợ khách hàng và nhân viên nhà hàng trong việc:

- Tra cứu bàn.
- Kiểm tra bàn khả dụng.
- Đặt, đổi, hủy đặt bàn.
- Bố trí bàn.
- Check-in.
- Cập nhật trạng thái bàn.
- Quản lý thông tin khách hàng.

**Hiện trạng [GĐ]:** việc đặt bàn có thể đang được quản lý thủ công, dễ xảy ra nhầm lịch hoặc đặt trùng. Cần khảo sát để xác nhận.

## 1.2. Actors

| Actor | Vai trò |
|---|---|
| **Khách hàng** | Tra cứu, kiểm tra khả dụng, đặt, đổi, hủy bàn |
| **Nhân viên** | Đặt hộ, bố trí bàn, check-in, cập nhật trạng thái, quản lý khách |
| **Quản trị viên** | Quản lý bàn và khu vực `[ĐX]` |

## 1.3. Phạm vi

**In Scope:**  
Tra cứu, kiểm tra khả dụng, đặt / xác nhận, đổi, hủy, bố trí bàn, check-in, cập nhật trạng thái và quản lý khách.

**Out of Scope:**  
Đặt món, thanh toán, khuyến mãi, tích điểm, quản lý nhiều chi nhánh.

---

# 2. Input → Processing → Output

## Input

| Nhóm | Dữ liệu |
|---|---|
| Khách hàng | Họ tên, SĐT, email |
| Đặt bàn | Thời gian bắt đầu, thời gian kết thúc, số người, khu vực, bàn mong muốn, ghi chú |
| Bàn | Mã bàn, sức chứa, khu vực, trạng thái |
| Vận hành | Mã đặt bàn, yêu cầu đổi / hủy, thông tin check-in |

## Processing

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

## Output

- Danh sách bàn khả dụng.
- Thông tin và mã đặt bàn.
- Kết quả đặt / đổi / hủy.
- Trạng thái đặt bàn và bàn.
- Thông tin check-in.

---

# 3. Business Rules

| ID | Business Rule | Nhãn |
|---|---|---|
| **BR-01** | Một bàn không được có hai đặt bàn hiệu lực chồng thời gian | [Đề bài] |
| **BR-02** | Số người không vượt quá sức chứa của bàn | [Đề bài] |
| **BR-03** | Chỉ bàn khả dụng mới được đặt | [Đề bài] |
| **BR-04** | Họ tên, SĐT, thời gian và số người là bắt buộc `[GĐ]` | [Đề bài] + [GĐ] |
| **BR-05** | Mỗi đặt bàn có một mã duy nhất | [ĐX] |
| **BR-06** | Chỉ đặt bàn còn hiệu lực mới được đổi / hủy | [GĐ] |
| **BR-07** | Khi đổi thời gian hoặc bàn phải kiểm tra lại khả dụng | [Đề bài] |
| **BR-08** | Chỉ đặt bàn hợp lệ mới được check-in | [Đề bài] |
| **BR-09** | Check-in phải cập nhật trạng thái đặt bàn và bàn | [Đề bài] |
| **BR-10** | Hệ thống phải tránh đặt trùng khi có nhiều yêu cầu đồng thời | [ĐX] |

### Trạng thái đặt bàn `[GĐ]`

```text
Confirmed → Checked-in → Completed
     └──────────────→ Cancelled
```

### Trạng thái bàn `[GĐ]`

```text
Available ↔ Occupied
Available ↔ Unavailable
```

> `Reserved` không được xem là trạng thái hiện tại của bàn; lịch đặt được xác định từ thông tin reservation.

---

# 4. Yêu cầu hệ thống (SRS)

## 4.1. Functional Requirements

| ID | Yêu cầu | Actor |
|---|---|---|
| **FR-01** | Tra cứu bàn theo khu vực, sức chứa và trạng thái | KH, NV |
| **FR-02** | Kiểm tra bàn khả dụng theo thời gian và số người | KH, NV |
| **FR-03** | Tạo và xác nhận đặt bàn, sinh mã đặt bàn | KH, NV |
| **FR-04** | Ngăn đặt trùng lịch | Hệ thống |
| **FR-05** | Đổi thông tin hoặc đổi bàn | KH, NV |
| **FR-06** | Hủy đặt bàn | KH, NV |
| **FR-07** | Bố trí / thay đổi bàn | NV, QTV |
| **FR-08** | Check-in | NV |
| **FR-09** | Cập nhật trạng thái bàn | NV, QTV |
| **FR-10** | Quản lý thông tin khách hàng | NV, QTV |
| **FR-11** | Thông báo kết quả thao tác | Hệ thống |
| **FR-12** | Quản lý bàn và khu vực | QTV |

## 4.2. Non-functional Requirements

| ID | Yêu cầu |
|---|---|
| **NFR-01** | Không xảy ra đặt trùng bàn khi nhiều yêu cầu được xử lý đồng thời |
| **NFR-02** | Chức năng của nhân viên / quản trị viên phải được xác thực và phân quyền |
| **NFR-03** | Bảo vệ thông tin cá nhân của khách hàng |
| **NFR-04** | Dữ liệu đặt bàn và trạng thái bàn phải nhất quán |

---

# 5. Assumptions

- **AS-01:** Hệ thống phục vụ một nhà hàng `[GĐ]`.
- **AS-02:** Mỗi đặt bàn gắn với một bàn `[GĐ]`.
- **AS-03:** Đặt bàn hợp lệ được xác nhận ngay `[GĐ]`.
- **AS-04:** Khách có thể tự đặt hoặc nhân viên đặt hộ `[GĐ]`.
- **AS-05:** Check-in do nhân viên thực hiện `[GĐ]`.
- **AS-06:** Khách đổi / hủy bằng mã đặt bàn + SĐT `[GĐ]`.

---

# 6. Open Questions

| ID | Câu hỏi cần xác nhận |
|---|---|
| **OQ-01** | Một lượt đặt bàn kéo dài bao lâu? |
| **OQ-02** | Khung giờ phục vụ và giới hạn đặt trước là gì? |
| **OQ-03** | Đặt bàn tự động xác nhận hay cần nhân viên duyệt? |
| **OQ-04** | Thời hạn đổi / hủy và phí hủy như thế nào? |
| **OQ-05** | Xử lý khách đến trễ và no-show như thế nào? |
| **OQ-06** | Có cho phép ghép nhiều bàn không? |
| **OQ-07** | Khách xác thực khi đổi / hủy bằng mã + SĐT hay OTP? |

---

# 7. Quy trình phát triển

## Đề xuất: Scrum

| Quy trình | Đánh giá |
|---|---|
| Waterfall | ❌ Khó thay đổi khi yêu cầu chưa ổn định |
| Agile | ✅ Phù hợp |
| **Scrum** | ✅ **Đề xuất lựa chọn** |
| Spiral | ⚠️ Tương đối phức tạp với phạm vi hệ thống |

### Lý do chọn Scrum

- Yêu cầu còn một số điểm cần xác nhận.
- Có thể phát triển theo từng Sprint.
- Dễ nhận phản hồi và điều chỉnh.
- Tính năng mới có thể đưa vào Product Backlog.
