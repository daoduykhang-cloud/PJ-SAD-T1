<mxfile host="app.diagrams.net" modified="2026-10-30T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="activity_diagram_sad" name="Activity Diagram">
    <mxGraphModel dx="1000" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Start Node -->
        <mxCell id="start" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="384" y="40" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Step 1: Open System -->
        <mxCell id="step1" value="Mở giao diện chức năng" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="329" y="110" width="140" height="50" as="geometry" />
        </mxCell>

        <!-- Step 2: Input Data -->
        <mxCell id="step2" value="Nhập thông tin yêu cầu" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="329" y="190" width="140" height="50" as="geometry" />
        </mxCell>

        <!-- Step 3: Validate -->
        <mxCell id="step3" value="Kiểm tra thông tin" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="329" y="270" width="140" height="50" as="geometry" />
        </mxCell>

        <!-- Decision: Valid? -->
        <mxCell id="decision1" value="Hợp lệ?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="349" y="350" width="100" height="60" as="geometry" />
        </mxCell>

        <!-- Error Step -->
        <mxCell id="steperror" value="Thông báo lỗi nhập liệu" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="150" y="355" width="140" height="50" as="geometry" />
        </mxCell>

        <!-- Step 4: Process & Save -->
        <mxCell id="step4" value="Xử lý và lưu dữ liệu vào CSDL" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="324" y="450" width="150" height="50" as="geometry" />
        </mxCell>

        <!-- Step 5: Return Result -->
        <mxCell id="step5" value="Hiển thị kết quả cho người dùng" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="324" y="530" width="150" height="50" as="geometry" />
        </mxCell>

        <!-- End Node -->
        <mxCell id="end" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="384" y="610" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Edges -->
        <mxCell id="e1" edge="1" parent="1" source="start" target="step1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1;">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e2" edge="1" parent="1" source="step1" target="step2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1;">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e3" edge="1" parent="1" source="step2" target="step3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1;">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e4" edge="1" parent="1" source="step3" target="decision1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1;">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_no" edge="1" parent="1" source="decision1" target="steperror" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1;" value="Không">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_retry" edge="1" parent="1" source="steperror" target="step2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="220" y="215" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="e_yes" edge="1" parent="1" source="decision1" target="step4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1;" value="Có">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e5" edge="1" parent="1" source="step4" target="step5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1;">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e6" edge="1" parent="1" source="step5" target="end" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=1;">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>