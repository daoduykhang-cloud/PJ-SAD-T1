<mxfile host="app.diagrams.net" modified="2026-09-30T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="activity-diagram-1" name="Activity_Diagram">
    <mxGraphModel dx="1000" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Swimlanes -->
        <mxCell id="lane_user" value="Người dùng (User)" style="swimlane;html=1;startSize=20;horizontal=0;collapsible=0;whiteSpace=wrap;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="220" height="720" as="geometry" />
        </mxCell>
        <mxCell id="lane_system" value="Hệ thống (System)" style="swimlane;html=1;startSize=20;horizontal=0;collapsible=0;whiteSpace=wrap;" vertex="1" parent="1">
          <mxGeometry x="260" y="40" width="240" height="720" as="geometry" />
        </mxCell>
        <mxCell id="lane_db" value="Cơ sở dữ liệu / Admin" style="swimlane;html=1;startSize=20;horizontal=0;collapsible=0;whiteSpace=wrap;" vertex="1" parent="1">
          <mxGeometry x="500" y="40" width="240" height="720" as="geometry" />
        </mxCell>

        <!-- User Swimlane Elements -->
        <mxCell id="start" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#000000;" vertex="1" parent="lane_user">
          <mxGeometry x="95" y="40" width="30" height="30" as="geometry" />
        </mxCell>

        <mxCell id="act_1" value="Nhập thông tin &amp;&#xa;Gửi yêu cầu / Tác vụ" style="html=1;whiteSpace=wrap;aspect=fixed;shape=rect;rounded=1;" vertex="1" parent="lane_user">
          <mxGeometry x="45" y="100" width="130" height="50" as="geometry" />
        </mxCell>

        <mxCell id="act_view_res" value="Nhận thông báo &amp;&#xa;Xem kết quả xử lý" style="html=1;whiteSpace=wrap;aspect=fixed;shape=rect;rounded=1;" vertex="1" parent="lane_user">
          <mxGeometry x="45" y="600" width="130" height="50" as="geometry" />
        </mxCell>

        <mxCell id="end" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane_user">
          <mxGeometry x="95" y="675" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- System Swimlane Elements -->
        <mxCell id="act_2" value="Tiếp nhận &amp;&#xa;Kiểm tra dữ liệu" style="html=1;whiteSpace=wrap;aspect=fixed;shape=rect;rounded=1;" vertex="1" parent="lane_system">
          <mxGeometry x="55" y="100" width="130" height="50" as="geometry" />
        </mxCell>

        <mxCell id="dec_1" value="Hợp lệ?" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="lane_system">
          <mxGeometry x="80" y="180" width="80" height="50" as="geometry" />
        </mxCell>

        <mxCell id="act_err" value="Hiển thị thông báo&#xa;lỗi nhập liệu" style="html=1;whiteSpace=wrap;aspect=fixed;shape=rect;rounded=1;" vertex="1" parent="lane_system">
          <mxGeometry x="55" y="270" width="130" height="50" as="geometry" />
        </mxCell>

        <mxCell id="act_3" value="Ghi nhận Yêu cầu&#xa;(Chờ phê duyệt)" style="html=1;whiteSpace=wrap;aspect=fixed;shape=rect;rounded=1;" vertex="1" parent="lane_system">
          <mxGeometry x="55" y="360" width="130" height="50" as="geometry" />
        </mxCell>

        <mxCell id="act_notify" value="Cập nhật trạng thái &amp;&#xa;Gửi phản hồi cho User" style="html=1;whiteSpace=wrap;aspect=fixed;shape=rect;rounded=1;" vertex="1" parent="lane_system">
          <mxGeometry x="55" y="600" width="130" height="50" as="geometry" />
        </mxCell>

        <!-- Admin/DB Swimlane Elements -->
        <mxCell id="act_4" value="Kiểm tra thông tin&#xa;&amp; Phê duyệt" style="html=1;whiteSpace=wrap;aspect=fixed;shape=rect;rounded=1;" vertex="1" parent="lane_db">
          <mxGeometry x="55" y="360" width="130" height="50" as="geometry" />
        </mxCell>

        <mxCell id="dec_2" value="Duyệt?" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="lane_db">
          <mxGeometry x="80" y="450" width="80" height="50" as="geometry" />
        </mxCell>

        <mxCell id="act_approve" value="Lưu CSDL:&#xa;Trạng thái &#34;Đã duyệt&#34;" style="html=1;whiteSpace=wrap;aspect=fixed;shape=rect;rounded=1;" vertex="1" parent="lane_db">
          <mxGeometry x="10" y="530" width="100" height="50" as="geometry" />
        </mxCell>

        <mxCell id="act_reject" value="Lưu CSDL:&#xa;Trạng thái &#34;Từ chối&#34;" style="html=1;whiteSpace=wrap;aspect=fixed;shape=rect;rounded=1;" vertex="1" parent="lane_db">
          <mxGeometry x="130" y="530" width="100" height="50" as="geometry" />
        </mxCell>

        <!-- Connectors -->
        <mxCell id="e1" edge="1" parent="1" source="start" target="act_1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" />
        <mxCell id="e2" edge="1" parent="1" source="act_1" target="act_2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" />
        <mxCell id="e3" edge="1" parent="1" source="act_2" target="dec_1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" />
        <mxCell id="e4" edge="1" parent="1" source="dec_1" target="act_err" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" value="Không" />
        <mxCell id="e5" edge="1" parent="1" source="act_err" target="act_1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" />
        <mxCell id="e6" edge="1" parent="1" source="dec_1" target="act_3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" value="Có" />
        <mxCell id="e7" edge="1" parent="1" source="act_3" target="act_4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" />
        <mxCell id="e8" edge="1" parent="1" source="act_4" target="dec_2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" />
        <mxCell id="e9" edge="1" parent="1" source="dec_2" target="act_approve" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" value="Đồng ý" />
        <mxCell id="e10" edge="1" parent="1" source="dec_2" target="act_reject" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" value="Từ chối" />
        <mxCell id="e11" edge="1" parent="1" source="act_approve" target="act_notify" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" />
        <mxCell id="e12" edge="1" parent="1" source="act_reject" target="act_notify" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" />
        <mxCell id="e13" edge="1" parent="1" source="act_notify" target="act_view_res" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" />
        <mxCell id="e14" edge="1" parent="1" source="act_view_res" target="end" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;" />

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>