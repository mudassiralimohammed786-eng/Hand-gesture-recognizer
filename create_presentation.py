import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Color Palette
    BG_COLOR = RGBColor(10, 25, 47)         # #0A192F Dark Navy
    CARD_BG = RGBColor(17, 34, 64)          # #112240 Card Navy
    CARD_BORDER = RGBColor(0, 229, 255)     # #00E5FF Cyan
    ACCENT_GREEN = RGBColor(16, 185, 129)   # #10B981 Emerald
    ACCENT_CYAN = RGBColor(0, 229, 255)     # #00E5FF Cyan
    ACCENT_GOLD = RGBColor(255, 193, 7)     # #FFC107 Gold
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(148, 163, 184)    # #94A3B8 Slate Gray

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="REAL-TIME HAND GESTURE RECOGNITION AI"):
        # Header banner text
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
        
        # Category subtitle
        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN
        
        # Main Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = "Arial"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.space_before = Pt(4)

    def add_card(slide, left, top, width, height, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Decorative top bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.7), Inches(1.2), Inches(0.08))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_CYAN
    bar.line.fill.background()

    # Title & Subtitle Box
    tbox = s1.shapes.add_textbox(Inches(0.8), Inches(1.0), Inches(11.7), Inches(3.2))
    tf1 = tbox.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "MAJOR INDUSTRIAL TRAINING PROJECT PRESENTATION"
    p0.font.name = "Arial"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_CYAN

    p1 = tf1.add_paragraph()
    p1.text = "REAL-TIME HAND GESTURE RECOGNITION &\nHUMAN-COMPUTER INTERACTION PLATFORM"
    p1.font.name = "Arial"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_before = Pt(10)

    p2 = tf1.add_paragraph()
    p2.text = "Powered by Google MediaPipe, OpenCV, WebAssembly 60 FPS Engine & Python Flask"
    p2.font.name = "Arial"
    p2.font.size = Pt(14)
    p2.font.color.rgb = ACCENT_GREEN
    p2.space_before = Pt(12)

    # Student Credential Card
    add_card(s1, Inches(0.8), Inches(4.5), Inches(5.6), Inches(2.3), ACCENT_CYAN)
    sbox = s1.shapes.add_textbox(Inches(1.0), Inches(4.65), Inches(5.2), Inches(2.0))
    stf = sbox.text_frame
    stf.word_wrap = True

    sp0 = stf.paragraphs[0]
    sp0.text = "PRESENTER CREDENTIALS"
    sp0.font.name = "Arial"
    sp0.font.size = Pt(11)
    sp0.font.bold = True
    sp0.font.color.rgb = ACCENT_CYAN

    sp1 = stf.add_paragraph()
    sp1.text = "Name: MD.Mudassir Ali"
    sp1.font.name = "Arial"
    sp1.font.size = Pt(16)
    sp1.font.bold = True
    sp1.font.color.rgb = TEXT_WHITE
    sp1.space_before = Pt(4)

    sp2 = stf.add_paragraph()
    sp2.text = "Registration No: 72312062"
    sp2.font.name = "Arial"
    sp2.font.size = Pt(14)
    sp2.font.bold = True
    sp2.font.color.rgb = ACCENT_GOLD
    sp2.space_before = Pt(3)

    sp3 = stf.add_paragraph()
    sp3.text = "B.Tech in Computer Science and Engineering (AI & DS)"
    sp3.font.name = "Arial"
    sp3.font.size = Pt(11.5)
    sp3.font.color.rgb = TEXT_MUTED
    sp3.space_before = Pt(4)

    # University Institution Card
    add_card(s1, Inches(6.8), Inches(4.5), Inches(5.7), Inches(2.3), ACCENT_GREEN)
    ubox = s1.shapes.add_textbox(Inches(7.0), Inches(4.65), Inches(5.3), Inches(2.0))
    utf = ubox.text_frame
    utf.word_wrap = True

    up0 = utf.paragraphs[0]
    up0.text = "ACADEMIC INSTITUTION"
    up0.font.name = "Arial"
    up0.font.size = Pt(11)
    up0.font.bold = True
    up0.font.color.rgb = ACCENT_GREEN

    up1 = utf.add_paragraph()
    up1.text = "CT UNIVERSITY"
    up1.font.name = "Arial"
    up1.font.size = Pt(18)
    up1.font.bold = True
    up1.font.color.rgb = TEXT_WHITE
    up1.space_before = Pt(4)

    up2 = utf.add_paragraph()
    up2.text = "Department of Computer Science and Engineering\nLudhiana (Punjab), India\nRecognized by UGC | www.ctuniversity.in"
    up2.font.name = "Arial"
    up2.font.size = Pt(11)
    up2.font.color.rgb = TEXT_MUTED
    up2.space_before = Pt(4)

    # =========================================================================
    # SLIDE 2: INTRODUCTION & MOTIVATION
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "1. Introduction & Motivation: The Need for Contactless HCI")

    # Left Column: The Problem
    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.1), RGBColor(239, 68, 68))
    box2_l = s2.shapes.add_textbox(Inches(1.0), Inches(1.95), Inches(5.2), Inches(4.8))
    tf2_l = box2_l.text_frame
    tf2_l.word_wrap = True

    p = tf2_l.paragraphs[0]
    p.text = "LIMITATIONS OF PHYSICAL INTERFACES"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(239, 68, 68)

    pts_l = [
        ("Pathogen Transmission & Hygiene", "Operating rooms, intensive care units, and sterile medical suites require surgeons to navigate scans without touching mice or screens."),
        ("Physical Wear & Hardware Breakdown", "Mechanical buttons, touchpads, and keyboards in high-traffic public kiosks (ATMs, ticketing) deteriorate rapidly."),
        ("Motor Accessibility Barriers", "Individuals with muscular dystrophy, tremors, or partial limb impairments struggle with fine-motor mouse manipulation."),
        ("Dangerous Industrial Environments", "Cleanrooms, chemical labs, and heavy robotics require hands-free spatial command triggers.")
    ]
    for title, desc in pts_l:
        p_t = tf2_l.add_paragraph()
        p_t.text = f"• {title}"
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.space_before = Pt(8)
        p_d = tf2_l.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_before = Pt(1)

    # Right Column: The Computer Vision Solution
    add_card(s2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1), ACCENT_CYAN)
    box2_r = s2.shapes.add_textbox(Inches(7.0), Inches(1.95), Inches(5.3), Inches(4.8))
    tf2_r = box2_r.text_frame
    tf2_r.word_wrap = True

    p = tf2_r.paragraphs[0]
    p.text = "THE SENSORLESS COMPUTER VISION SOLUTION"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    pts_r = [
        ("No Specialized Hardware Needed", "Operates entirely on commodity monocular RGB webcams without depth sensors, Leap Motion, or data gloves."),
        ("Google MediaPipe 3D Landmark Model", "Regresses 21 3D landmarks in real time, capturing joint flexions, finger spreads, and spatial depths."),
        ("Zero-Latency Dual Deployment", "Native Windows OpenCV application + high-speed 60 FPS browser WebAssembly web portal."),
        ("Deterministic Mathematical Engine", "Coordinate vector geometry provides 100% deterministic, instant gesture classification without black-box lag.")
    ]
    for title, desc in pts_r:
        p_t = tf2_r.add_paragraph()
        p_t.text = f"✓ {title}"
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = ACCENT_GREEN
        p_t.space_before = Pt(8)
        p_d = tf2_r.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_before = Pt(1)

    # =========================================================================
    # SLIDE 3: OBJECTIVES & SCOPE
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "2. Project Objectives & Architectural Scope")

    cards3 = [
        ("Sub-20ms Real-Time Inference", "Achieve seamless continuous inference (>30 FPS on CPU, 60 FPS on WebAssembly GPU) without perceptible lag.", ACCENT_CYAN),
        ("Continuous 21 3D Landmark Tracking", "Accurately predict 21 coordinates (X, Y, Z depth) per frame even during rapid hand rotations or transitions.", ACCENT_GREEN),
        ("Invariant Geometric Classifier", "Formulate relative bone-joint vectors that classify gestures independent of hand distance or hand size.", ACCENT_GOLD),
        ("DirectShow Camera Acceleration", "Implement hardware acquisition hooks to cut Windows OpenCV camera startup delay from 9.2s to <450ms.", RGBColor(168, 85, 247)),
        ("Dual Platform Interactivity", "Provide both an offline desktop native window and a modern interactive web portal with live analytics.", ACCENT_CYAN),
        ("HUD Metrics & Visual Feedback", "Display live 5-finger state bitmasks, real-time FPS meters, snapshot utilities, and gesture activity logs.", ACCENT_GREEN)
    ]

    for i, (title, desc, color) in enumerate(cards3):
        r = i // 3
        c = i % 3
        x = Inches(0.8 + c * 4.0)
        y = Inches(1.8 + r * 2.6)
        add_card(s3, x, y, Inches(3.7), Inches(2.3), color)
        tbox = s3.shapes.add_textbox(x + Inches(0.2), y + Inches(0.2), Inches(3.3), Inches(1.9))
        tf = tbox.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        p0.text = f"0{i+1}. {title}"
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = color
        
        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(10)
        p1.font.color.rgb = TEXT_MUTED
        p1.space_before = Pt(8)

    # =========================================================================
    # SLIDE 4: SYSTEM ARCHITECTURE
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "3. End-to-End System Processing Architecture")

    # Insert Architecture Diagram
    if os.path.exists("presentation_assets/diagram_architecture.png"):
        s4.shapes.add_picture("presentation_assets/diagram_architecture.png", Inches(0.8), Inches(1.7), Inches(11.7), Inches(3.3))

    # Architecture Explanation Cards below
    add_card(s4, Inches(0.8), Inches(5.2), Inches(5.7), Inches(1.8), ACCENT_CYAN)
    tbox_a1 = s4.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(5.3), Inches(1.5))
    tf_a1 = tbox_a1.text_frame
    tf_a1.word_wrap = True
    p = tf_a1.paragraphs[0]
    p.text = "TWO-STAGE CONVOLUTIONAL PIPELINE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p2 = tf_a1.add_paragraph()
    p2.text = "1. BlazePalm Detector: Detects the 2D bounding palm box once.\n2. Hand Landmark Model: Regresses 21 3D landmarks within the box.\nBenefit: Avoids expensive full-frame scanning on every single frame."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(4)

    add_card(s4, Inches(6.8), Inches(5.2), Inches(5.7), Inches(1.8), ACCENT_GREEN)
    tbox_a2 = s4.shapes.add_textbox(Inches(7.0), Inches(5.3), Inches(5.3), Inches(1.5))
    tf_a2 = tbox_a2.text_frame
    tf_a2.word_wrap = True
    p = tf_a2.paragraphs[0]
    p.text = "VECTOR EXTRACTION & HUD OVERLAY"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p2 = tf_a2.add_paragraph()
    p2.text = "• Relative Joint Coordinates: Extracted and evaluated in real time.\n• Deterministic Classification: Maps finger bitmasks to gestures.\n• Zero-Lag Rendering: In-browser WebAssembly canvas or OpenCV GUI."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(4)

    # =========================================================================
    # SLIDE 5: 21 LANDMARKS TOPOLOGY
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "4. MediaPipe 21 Hand Landmarks Topology")

    # Left: Image
    if os.path.exists("presentation_assets/diagram_landmarks.png"):
        s5.shapes.add_picture("presentation_assets/diagram_landmarks.png", Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.4))

    # Right: Anatomical breakdown cards
    add_card(s5, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.4), ACCENT_CYAN)
    tbox_topo = s5.shapes.add_textbox(Inches(7.1), Inches(1.75), Inches(5.2), Inches(5.1))
    tf_topo = tbox_topo.text_frame
    tf_topo.word_wrap = True

    p = tf_topo.paragraphs[0]
    p.text = "ANATOMICAL SKELETAL STRUCTURE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    topo_points = [
        ("Base Reference", "Landmark 0 (Wrist root coordinate)"),
        ("Thumb (4 points)", "1 (CMC), 2 (MCP), 3 (IP), 4 (Tip)"),
        ("Index Finger (4 points)", "5 (MCP), 6 (PIP), 7 (DIP), 8 (Tip)"),
        ("Middle Finger (4 points)", "9 (MCP), 10 (PIP), 11 (DIP), 12 (Tip)"),
        ("Ring Finger (4 points)", "13 (MCP), 14 (PIP), 15 (DIP), 16 (Tip)"),
        ("Pinky Finger (4 points)", "17 (MCP), 18 (PIP), 19 (DIP), 20 (Tip)"),
        ("Tip Landmarks (TIP_IDS)", "[4, 8, 12, 16, 20] used for status detection")
    ]
    for group, desc in topo_points:
        p_g = tf_topo.add_paragraph()
        p_g.text = f"• {group}:"
        p_g.font.size = Pt(10.5)
        p_g.font.bold = True
        p_g.font.color.rgb = ACCENT_GREEN
        p_g.space_before = Pt(6)
        p_d = tf_topo.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = TEXT_WHITE
        p_d.space_before = Pt(1)

    # =========================================================================
    # SLIDE 6: MATHEMATICAL CLASSIFICATION ENGINE
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "5. Mathematical Classification Engine & Geometry")

    # Left: Formulas
    add_card(s6, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1), ACCENT_GOLD)
    tbox_f = s6.shapes.add_textbox(Inches(1.0), Inches(1.95), Inches(5.3), Inches(4.8))
    tf_f = tbox_f.text_frame
    tf_f.word_wrap = True

    p = tf_f.paragraphs[0]
    p.text = "COORDINATE GEOMETRY FORMULATION"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD

    f_points = [
        ("Screen Coordinate Origin", "The image origin (0, 0) is top-left. Y values increase downwards; X values increase to the right."),
        ("Four Fingers Extension Rule", "For finger i in [1, 2, 3, 4] (Index, Middle, Ring, Pinky):\nf_i = 1  IF  y[TIP_IDS[i]] < y[TIP_IDS[i] - 2]  ELSE  0\n(If the tip Y is smaller than the PIP joint Y, the finger is extended upwards)."),
        ("Thumb Extension Rule", "The thumb flexes horizontally:\nf_0 = 1  IF  x[TIP_IDS[0]] < x[TIP_IDS[0] - 1]  ELSE  0\n(Evaluates lateral extension across the horizontal axis)."),
        ("Feature Vector Representation", "Produces a 5-digit binary state vector:\nF = [f_0, f_1, f_2, f_3, f_4]  where f_i in {0, 1}")
    ]
    for title, desc in f_points:
        p_t = tf_f.add_paragraph()
        p_t.text = title
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.space_before = Pt(8)
        p_d = tf_f.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_before = Pt(2)

    # Right: Python Implementation Code Box
    add_card(s6, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1), ACCENT_CYAN)
    tbox_code = s6.shapes.add_textbox(Inches(7.0), Inches(1.95), Inches(5.3), Inches(4.8))
    tf_code = tbox_code.text_frame
    tf_code.word_wrap = True

    p = tf_code.paragraphs[0]
    p.text = "CORE ALGORITHM (Python & JavaScript)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    code_snippet = (
        "TIP_IDS = [4, 8, 12, 16, 20]\n\n"
        "def fingers_up(lm):\n"
        "    fingers = []\n"
        "    # Thumb (lateral comparison)\n"
        "    fingers.append(1 if lm[4].x < lm[3].x else 0)\n"
        "    \n"
        "    # 4 Fingers (vertical height comparison)\n"
        "    for i in range(1, 5):\n"
        "        fingers.append(1 if lm[TIP_IDS[i]].y < lm[TIP_IDS[i]-2].y else 0)\n"
        "    \n"
        "    return fingers  # e.g., [0, 1, 1, 0, 0] for Peace\n\n"
        "def gesture(f):\n"
        "    if sum(f) == 0: return 'Fist'\n"
        "    if sum(f) == 5: return 'Open Palm'\n"
        "    if f == [0, 1, 0, 0, 0]: return 'Point'\n"
        "    if f == [0, 1, 1, 0, 0]: return 'Peace'\n"
        "    if f == [1, 0, 0, 0, 0]: return 'Thumbs Up'\n"
        "    return f'Custom {f}'"
    )
    p_c = tf_code.add_paragraph()
    p_c.text = code_snippet
    p_c.font.name = "Consolas"
    p_c.font.size = Pt(8.5)
    p_c.font.color.rgb = ACCENT_GREEN
    p_c.space_before = Pt(8)

    # =========================================================================
    # SLIDE 7: RECOGNIZED GESTURE CATALOG
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "6. Core Recognized Gestures & Bitmask Mappings")

    # Insert Gesture cards diagram
    if os.path.exists("presentation_assets/diagram_gestures.png"):
        s7.shapes.add_picture("presentation_assets/diagram_gestures.png", Inches(0.8), Inches(1.7), Inches(11.7), Inches(4.5))

    # Caption bottom card
    add_card(s7, Inches(0.8), Inches(6.3), Inches(11.7), Inches(0.9), ACCENT_CYAN)
    tbox_cap = s7.shapes.add_textbox(Inches(1.0), Inches(6.35), Inches(11.3), Inches(0.8))
    tf_cap = tbox_cap.text_frame
    tf_cap.word_wrap = True
    p = tf_cap.paragraphs[0]
    p.text = "EXTENSIBLE CLASSIFIER ARCHITECTURE: Beyond the 6 core standard gestures, any 5-digit permutation (32 possible bitmask states) can be mapped to custom application commands (e.g., volume control, slide navigation, robotic actuation)."
    p.font.size = Pt(9.5)
    p.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 8: DESKTOP APPLICATION (OPENCV + DIRECTSHOW)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "7. Native Desktop Pipeline: OpenCV & DirectShow")

    cards8 = [
        ("DirectShow Acceleration", "Windows standard MSMF introduces 7-10s init delays. Forcing cv2.CAP_DSHOW cuts startup to <450ms.", ACCENT_CYAN),
        ("Frame Flipping & Mirroring", "Applies cv2.flip(frame, 1) to mirror webcam feed, creating natural interactive feedback for users.", ACCENT_GREEN),
        ("Color Space Conversion", "Converts BGR to RGB for MediaPipe inference, then back to BGR for OpenCV display rendering.", ACCENT_GOLD),
        ("HUD Text & Skeleton Overlay", "Renders skeletal connectors, landmark coordinates, and gesture labels dynamically on video.", RGBColor(168, 85, 247)),
        ("Clean Shutdown & Signal Handling", "Graceful resource release with cap.release() and cv2.destroyAllWindows() upon pressing 'q' or 'Esc'.", ACCENT_CYAN),
        ("One-Click Batch Execution", "Bundled with run.bat, automatically launching the isolated Python 3.11 environment with zero setup.", ACCENT_GREEN)
    ]

    for i, (title, desc, color) in enumerate(cards8):
        r = i // 3
        c = i % 3
        x = Inches(0.8 + c * 4.0)
        y = Inches(1.8 + r * 2.6)
        add_card(s8, x, y, Inches(3.7), Inches(2.3), color)
        tbox = s8.shapes.add_textbox(x + Inches(0.2), y + Inches(0.2), Inches(3.3), Inches(1.9))
        tf = tbox.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = color
        
        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(10)
        p1.font.color.rgb = TEXT_MUTED
        p1.space_before = Pt(8)

    # =========================================================================
    # SLIDE 9: WEB APPLICATION PORTAL
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "8. High-Performance Web Portal (60 FPS WebAssembly)")

    cards9 = [
        ("Client-Side WebAssembly (60 FPS)", "Direct browser GPU acceleration using @mediapipe/camera_utils and WebGL shaders with zero video compression lag.", ACCENT_CYAN),
        ("Glassmorphic Dark Cyber HUD", "Ultra-modern responsive UI featuring glowing neon badges, animated emoji transitions, and dark background styling.", ACCENT_GREEN),
        ("5-Finger Real-Time State Grid", "Interactive indicator pills for Thumb, Index, Middle, Ring, and Pinky showing UP vs DOWN states in real time.", ACCENT_GOLD),
        ("Integrated Snapshot Camera Tool", "Instant high-resolution photo capture with automated timestamp and recognized gesture watermarking.", RGBColor(168, 85, 247)),
        ("Dual-Engine Architecture", "Seamlessly toggle between Browser WebAssembly Mode and Python OpenCV Backend Streaming via /video_feed.", ACCENT_CYAN),
        ("Python Flask Microservice", "Lightweight backend providing REST status APIs (/api/status), file downloads, and automated browser launch.", ACCENT_GREEN)
    ]

    for i, (title, desc, color) in enumerate(cards9):
        r = i // 3
        c = i % 3
        x = Inches(0.8 + c * 4.0)
        y = Inches(1.8 + r * 2.6)
        add_card(s9, x, y, Inches(3.7), Inches(2.3), color)
        tbox = s9.shapes.add_textbox(x + Inches(0.2), y + Inches(0.2), Inches(3.3), Inches(1.9))
        tf = tbox.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = color
        
        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(10)
        p1.font.color.rgb = TEXT_MUTED
        p1.space_before = Pt(8)

    # =========================================================================
    # SLIDE 10: KEY ENGINEERING CHALLENGES & SOLUTIONS
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "9. Key Engineering Challenges & Technical Solutions")

    challenges = [
        ("Challenge 1: MediaPipe 1.x solutions API Deprecation",
         "Issue: Recent MediaPipe 1.x releases removed mp.solutions.hands, causing AttributeError.\n"
         "Solution: Pinned mediapipe<=0.10.14 with Python 3.11 in a dedicated isolated virtual environment, restoring full API stability without recompilation.",
         ACCENT_CYAN),
        ("Challenge 2: Windows MSMF Camera Driver Freeze",
         "Issue: Default OpenCV camera capture stalled for 7-10 seconds due to Microsoft Media Foundation.\n"
         "Solution: Implemented DirectShow hardware initialization: cv2.VideoCapture(0, cv2.CAP_DSHOW), reducing camera delay from 9,200ms to under 450ms.",
         ACCENT_GREEN),
        ("Challenge 3: Video Streaming Network Bottleneck",
         "Issue: Streaming MJPEG video from Python to browser saturated network bandwidth and restricted FPS to ~20.\n"
         "Solution: Offloaded computer vision inference to client-side WebAssembly directly on the user's GPU, achieving native 60 FPS with zero streaming lag.",
         ACCENT_GOLD)
    ]

    for i, (title, desc, color) in enumerate(challenges):
        y = Inches(1.8 + i * 1.8)
        add_card(s10, Inches(0.8), y, Inches(11.7), Inches(1.6), color)
        tbox = s10.shapes.add_textbox(Inches(1.0), y + Inches(0.15), Inches(11.3), Inches(1.3))
        tf = tbox.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = color
        
        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(10)
        p1.font.color.rgb = TEXT_WHITE
        p1.space_before = Pt(4)

    # =========================================================================
    # SLIDE 11: PERFORMANCE EVALUATION & BENCHMARKS
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "10. Performance Evaluation & Benchmarking")

    # Insert Benchmark Diagram
    if os.path.exists("presentation_assets/diagram_benchmarks.png"):
        s11.shapes.add_picture("presentation_assets/diagram_benchmarks.png", Inches(0.8), Inches(1.7), Inches(6.8), Inches(5.1))

    # Right: Metric Summary Card
    add_card(s11, Inches(7.8), Inches(1.7), Inches(4.7), Inches(5.1), ACCENT_GREEN)
    tbox_m = s11.shapes.add_textbox(Inches(8.0), Inches(1.85), Inches(4.3), Inches(4.8))
    tf_m = tbox_m.text_frame
    tf_m.word_wrap = True

    p = tf_m.paragraphs[0]
    p.text = "QUANTITATIVE BENCHMARK SUMMARY"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    metrics = [
        ("Framerate (FPS)", "Desktop: 38 FPS\nWebAssembly GPU: 60 FPS (V-Sync locked)"),
        ("Inference Latency", "Desktop: 21 ms\nWebAssembly GPU: 10 ms (Sub-frame)"),
        ("Camera Init Time", "MSMF Default: 9,200 ms\nDirectShow Backend: 420 ms"),
        ("CPU Utilization", "Desktop Python: ~12% (Intel i7)\nWeb Portal: ~6% (GPU offloaded)"),
        ("Recognition Accuracy", ">98% under normal lighting across all 6 core gestures.")
    ]
    for label, val in metrics:
        p_l = tf_m.add_paragraph()
        p_l.text = f"• {label}:"
        p_l.font.size = Pt(10)
        p_l.font.bold = True
        p_l.font.color.rgb = ACCENT_CYAN
        p_l.space_before = Pt(6)
        p_v = tf_m.add_paragraph()
        p_v.text = val
        p_v.font.size = Pt(9)
        p_v.font.color.rgb = TEXT_WHITE
        p_v.space_before = Pt(1)

    # =========================================================================
    # SLIDE 12: REAL-WORLD APPLICATIONS & FUTURE SCOPE
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "11. Real-World Applications & Future Horizons")

    apps = [
        ("Sterile Healthcare Systems", "Touchless browsing of MRI/CT radiological imaging in surgery suites without breaking aseptic glove protocols.", ACCENT_CYAN),
        ("Sanitary Public Kiosks & ATMs", "Contactless interaction in airport ticketing, banking ATMs, and transit hubs, preventing cross-contamination.", ACCENT_GREEN),
        ("Motor Accessibility Aids", "Empowers individuals with mobility limitations or tremors to control computers via simple hand signals.", ACCENT_GOLD),
        ("Spatial Gaming & WebXR", "Direct touchless gesture interaction for virtual, augmented, and spatial computing headsets without controllers.", RGBColor(168, 85, 247)),
        ("Temporal Gesture Tracking (HMM/TCN)", "Future Scope: Expanding from static postures to temporal motions (swipe, wave, pinch-to-zoom).", ACCENT_CYAN),
        ("Robotic Arm Teleoperation", "Future Scope: Mapping 3D hand coordinates to industrial ROS (Robot Operating System) robotic manipulators.", ACCENT_GREEN)
    ]

    for i, (title, desc, color) in enumerate(apps):
        r = i // 3
        c = i % 3
        x = Inches(0.8 + c * 4.0)
        y = Inches(1.8 + r * 2.6)
        add_card(s12, x, y, Inches(3.7), Inches(2.3), color)
        tbox = s12.shapes.add_textbox(x + Inches(0.2), y + Inches(0.2), Inches(3.3), Inches(1.9))
        tf = tbox.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = color
        
        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(10)
        p1.font.color.rgb = TEXT_MUTED
        p1.space_before = Pt(8)

    # =========================================================================
    # SLIDE 13: CONCLUSION & Q&A DEFENSE
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13)

    # Center Hero Card
    add_card(s13, Inches(1.5), Inches(1.0), Inches(10.3), Inches(5.5), ACCENT_CYAN)
    tbox_concl = s13.shapes.add_textbox(Inches(1.8), Inches(1.3), Inches(9.7), Inches(5.0))
    tf_c = tbox_concl.text_frame
    tf_c.word_wrap = True

    p0 = tf_c.paragraphs[0]
    p0.text = "CONCLUSION & VIVA DEFENSE"
    p0.font.name = "Arial"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_CYAN
    p0.alignment = PP_ALIGN.CENTER

    p1 = tf_c.add_paragraph()
    p1.text = "Thank You!"
    p1.font.name = "Arial"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_before = Pt(8)
    p1.alignment = PP_ALIGN.CENTER

    p2 = tf_c.add_paragraph()
    p2.text = "Real-Time Hand Gesture Recognition & Human-Computer Interaction Platform"
    p2.font.name = "Arial"
    p2.font.size = Pt(14)
    p2.font.color.rgb = ACCENT_GREEN
    p2.space_before = Pt(4)
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf_c.add_paragraph()
    p3.text = "Successfully engineered a robust, sensorless, dual-mode computer vision interaction system\nachieving 60 FPS GPU-accelerated gesture recognition with sub-20ms inference latency."
    p3.font.name = "Arial"
    p3.font.size = Pt(11)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(12)
    p3.alignment = PP_ALIGN.CENTER

    # Presenter Box in conclusion
    p4 = tf_c.add_paragraph()
    p4.text = "MD.Mudassir Ali  |  Reg. No: 72312062"
    p4.font.name = "Arial"
    p4.font.size = Pt(16)
    p4.font.bold = True
    p4.font.color.rgb = ACCENT_GOLD
    p4.space_before = Pt(20)
    p4.alignment = PP_ALIGN.CENTER

    p5 = tf_c.add_paragraph()
    p5.text = "B.Tech in Computer Science and Engineering (AI & DS)\nCT University, Ludhiana (Punjab), India"
    p5.font.name = "Arial"
    p5.font.size = Pt(11.5)
    p5.font.color.rgb = TEXT_WHITE
    p5.space_before = Pt(4)
    p5.alignment = PP_ALIGN.CENTER

    p6 = tf_c.add_paragraph()
    p6.text = "Open for Questions & Technical Discussion"
    p6.font.name = "Arial"
    p6.font.size = Pt(12)
    p6.font.bold = True
    p6.font.color.rgb = ACCENT_CYAN
    p6.space_before = Pt(16)
    p6.alignment = PP_ALIGN.CENTER

    # Save output
    output_pptx = "HAND_GESTURE_RECOGNITION_PRESENTATION_MD_MUDASSIR_ALI.pptx"
    prs.save(output_pptx)
    print(f"PowerPoint Presentation successfully saved: {output_pptx}")

if __name__ == '__main__':
    build_presentation()

