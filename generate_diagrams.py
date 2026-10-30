import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

os.makedirs("presentation_assets", exist_ok=True)

# Set global styles
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'
plt.rcParams['axes.linewidth'] = 0.8

# 1. 21-LANDMARKS DIAGRAM
def create_landmarks_diagram():
    fig, ax = plt.subplots(figsize=(7, 6.2), dpi=200, facecolor='#0D1B2A')
    ax.set_facecolor('#0D1B2A')
    
    # 21 Landmark approximate 2D coordinates for an open palm
    coords = {
        0: (0.50, 0.12),  # Wrist
        1: (0.39, 0.22),  # Thumb CMC
        2: (0.30, 0.32),  # Thumb MCP
        3: (0.22, 0.42),  # Thumb IP
        4: (0.15, 0.50),  # Thumb Tip
        5: (0.40, 0.50),  # Index MCP
        6: (0.37, 0.65),  # Index PIP
        7: (0.35, 0.77),  # Index DIP
        8: (0.33, 0.88),  # Index Tip
        9: (0.50, 0.53),  # Middle MCP
        10: (0.50, 0.69), # Middle PIP
        11: (0.50, 0.82), # Middle DIP
        12: (0.50, 0.94), # Middle Tip
        13: (0.60, 0.50), # Ring MCP
        14: (0.62, 0.65), # Ring PIP
        15: (0.64, 0.77), # Ring DIP
        16: (0.65, 0.87), # Ring Tip
        17: (0.70, 0.45), # Pinky MCP
        18: (0.75, 0.56), # Pinky PIP
        19: (0.79, 0.67), # Pinky DIP
        20: (0.82, 0.77), # Pinky Tip
    }
    
    connections = [
        # Palm base
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 7), (7, 8),
        (5, 9), (9, 10), (10, 11), (11, 12),
        (9, 13), (13, 14), (14, 15), (15, 16),
        (13, 17), (17, 18), (18, 19), (19, 20),
        (0, 17)
    ]
    
    # Draw bone connections
    for start, end in connections:
        x_vals = [coords[start][0], coords[end][0]]
        y_vals = [coords[start][1], coords[end][1]]
        ax.plot(x_vals, y_vals, color='#00E5FF', linewidth=3.5, alpha=0.85, zorder=2)
    
    # Draw landmarks
    tip_ids = [4, 8, 12, 16, 20]
    for idx, (x, y) in coords.items():
        is_tip = idx in tip_ids
        color = '#FF0055' if is_tip else '#00FF66'
        size = 140 if is_tip else 90
        ax.scatter(x, y, s=size, color=color, edgecolors='#FFFFFF', linewidth=1.5, zorder=3)
        ax.text(x + 0.025, y - 0.015, f"{idx}", color='#FFFFFF', fontsize=9, fontweight='bold', zorder=4)
        
    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(0.05, 1.02)
    ax.axis('off')
    ax.set_title("MediaPipe 21 Hand Landmarks Topology", color='#FFFFFF', fontsize=14, fontweight='bold', pad=15)
    
    # Legend
    ax.plot([], [], 'o', color='#FF0055', label='Fingertip Landmarks (TIP_IDS: 4, 8, 12, 16, 20)', markersize=8)
    ax.plot([], [], 'o', color='#00FF66', label='Joint Landmarks (MCP, PIP, DIP, Wrist)', markersize=8)
    ax.plot([], [], '-', color='#00E5FF', label='Skeletal Bone Connections', linewidth=2.5)
    ax.legend(loc='lower center', facecolor='#1B263B', edgecolor='#415A77', labelcolor='#E0E1DD', fontsize=8.5, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig("presentation_assets/diagram_landmarks.png", facecolor='#0D1B2A')
    plt.close()

# 2. SYSTEM ARCHITECTURE DIAGRAM
def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=200, facecolor='#0D1B2A')
    ax.set_facecolor('#0D1B2A')
    
    steps = [
        ("1. Video Capture", "RGB Camera Feed\nDirectShow / WebRTC", "#1F4068"),
        ("2. Palm Detection", "BlazePalm Detector\nIdentifies Hand ROI", "#162447"),
        ("3. 3D Landmark Model", "Regresses 21 3D Points\n(X, Y, Z Depth)", "#1B1A47"),
        ("4. Vector Geometry", "Calculates relative\n(Y_tip < Y_pip) bitmask", "#3A0088"),
        ("5. Gesture Classifier", "Maps 5-bit array to\nFist, Palm, Peace, etc.", "#E43F5A"),
        ("6. UI / HUD Display", "60 FPS Web Portal\nor Desktop Window", "#00B4D8")
    ]
    
    n = len(steps)
    box_w = 1.25
    box_h = 1.6
    spacing = 1.48
    start_x = 0.5
    y = 1.5
    
    for i, (title, desc, color) in enumerate(steps):
        x = start_x + i * spacing
        rect = FancyBboxPatch((x, y), box_w, box_h, boxstyle="round,pad=0.03", facecolor=color, edgecolor='#00E5FF', linewidth=1.8, zorder=2)
        ax.add_patch(rect)
        ax.text(x + box_w/2, y + 1.2, title, color='#FFFFFF', fontsize=9.2, fontweight='bold', ha='center', va='center', zorder=3)
        ax.text(x + box_w/2, y + 0.6, desc, color='#E0E1DD', fontsize=7.8, ha='center', va='center', zorder=3)
        
        # Arrow
        if i < n - 1:
            ax.annotate('', xy=(x + box_w + spacing - box_w, y + box_h/2), xytext=(x + box_w, y + box_h/2),
                        arrowprops=dict(arrowstyle="->", color='#00FF66', lw=2.5, mutation_scale=15), zorder=4)
            
    ax.set_xlim(0.2, start_x + (n - 1) * spacing + box_w + 0.3)
    ax.set_ylim(0.8, 3.8)
    ax.axis('off')
    ax.set_title("End-to-End Real-Time System Processing Architecture", color='#FFFFFF', fontsize=13, fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig("presentation_assets/diagram_architecture.png", facecolor='#0D1B2A')
    plt.close()

# 3. BENCHMARK COMPARISON CHART
def create_benchmark_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 4.2), dpi=200, facecolor='#0D1B2A')
    for ax in [ax1, ax2]:
        ax.set_facecolor('#112233')
        ax.grid(axis='y', linestyle='--', alpha=0.3, color='#888888')
        ax.tick_params(colors='#FFFFFF', labelsize=9)
        for spine in ax.spines.values():
            spine.set_color('#445566')

    categories = ['Desktop Native\n(Python/OpenCV)', 'Web Portal\n(WebAssembly GPU)']
    
    # 1. FPS comparison
    fps_values = [38, 60]
    bars1 = ax1.bar(categories, fps_values, color=['#00B4D8', '#00FF66'], width=0.45, edgecolor='#FFFFFF', linewidth=1)
    ax1.set_ylabel("Frames Per Second (FPS)", color='#FFFFFF', fontsize=10, fontweight='bold')
    ax1.set_title("Framerate Performance (Higher is Better)", color='#FFFFFF', fontsize=10.5, fontweight='bold', pad=10)
    ax1.set_ylim(0, 75)
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{yval} FPS", ha='center', va='bottom', color='#FFFFFF', fontweight='bold', fontsize=9.5)

    # 2. Latency comparison
    latency_values = [21, 10]
    bars2 = ax2.bar(categories, latency_values, color=['#E63946', '#06D6A0'], width=0.45, edgecolor='#FFFFFF', linewidth=1)
    ax2.set_ylabel("Latency in Milliseconds (ms)", color='#FFFFFF', fontsize=10, fontweight='bold')
    ax2.set_title("Inference Latency (Lower is Better)", color='#FFFFFF', fontsize=10.5, fontweight='bold', pad=10)
    ax2.set_ylim(0, 30)
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f"{yval} ms", ha='center', va='bottom', color='#FFFFFF', fontweight='bold', fontsize=9.5)

    plt.tight_layout()
    plt.savefig("presentation_assets/diagram_benchmarks.png", facecolor='#0D1B2A')
    plt.close()

# 4. GESTURE CARDS DIAGRAM
def create_gesture_cards_diagram():
    fig, ax = plt.subplots(figsize=(9, 4.2), dpi=200, facecolor='#0D1B2A')
    ax.set_facecolor('#0D1B2A')
    
    gestures = [
        ("Fist", "[0, 0, 0, 0, 0]", "All fingers folded", "#334155"),
        ("Open Palm", "[1, 1, 1, 1, 1]", "All 5 digits extended", "#059669"),
        ("Point", "[0, 1, 0, 0, 0]", "Index up; others folded", "#0284C7"),
        ("Peace", "[0, 1, 1, 0, 0]", "Index & Middle up", "#7C3AED"),
        ("Thumbs Up", "[1, 0, 0, 0, 0]", "Thumb lateral up", "#D97706"),
        ("Rock On", "[0, 1, 0, 0, 1]", "Index & Pinky up", "#DC2626")
    ]
    
    card_w = 2.4
    card_h = 1.3
    cols = 3
    spacing_x = 2.8
    spacing_y = 1.7
    
    for idx, (name, pattern, desc, color) in enumerate(gestures):
        r = idx // cols
        c = idx % cols
        x = 0.5 + c * spacing_x
        y = 2.2 - r * spacing_y
        
        rect = FancyBboxPatch((x, y), card_w, card_h, boxstyle="round,pad=0.03", facecolor=color, edgecolor='#00E5FF', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + card_w/2, y + 0.95, name, color='#FFFFFF', fontsize=11, fontweight='bold', ha='center', va='center')
        ax.text(x + card_w/2, y + 0.55, pattern, color='#FDE047', fontsize=9.5, fontweight='bold', fontfamily='monospace', ha='center', va='center')
        ax.text(x + card_w/2, y + 0.22, desc, color='#E2E8F0', fontsize=8, ha='center', va='center')
        
    ax.set_xlim(0.2, 9.0)
    ax.set_ylim(0.2, 3.8)
    ax.axis('off')
    ax.set_title("Core Recognized Gestures & Finger Bitmask Mappings", color='#FFFFFF', fontsize=13, fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig("presentation_assets/diagram_gestures.png", facecolor='#0D1B2A')
    plt.close()

if __name__ == '__main__':
    create_landmarks_diagram()
    create_architecture_diagram()
    create_benchmark_diagram()
    create_gesture_cards_diagram()
    print("All diagrams generated successfully!")
