import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Sentient-EduCore Interactive Sandbox",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for ergonomic UI styling
st.markdown("""
<style>
    .main-title { font-size: 26px; font-weight: 700; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size: 15px; color: #4B5563; margin-bottom: 20px; }
    .metric-card { background-color: #F3F4F6; padding: 15px; border-radius: 8px; border-left: 5px solid #2563EB; }
    .cbt-box { background-color: #FDF2F8; padding: 18px; border-radius: 8px; border: 1px solid #F472B6; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🛡️ Sentient-EduCore: Affective Ergonomics Sandbox</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Interdisciplinary Applied Framework: Computer Science & AI – Workplace Psychology – Pedagogical Sciences</div>', unsafe_allow_html=True)

# 4 Core Architectural Tabs matching the paper
tab1, tab2, tab3, tab4 = st.tabs([
    "📝 Tab 1: Task-Agent (RAG Scaffolding)", 
    "🚫 Tab 2: Boundary-Guardian (Firewall)", 
    "🧘 Tab 3: Affective Telemetry (In-Situ CBT)", 
    "📊 Tab 4: Policy Dashboard (Executive Heatmap)"
])

# =========================================================================
# TAB 1: TASK-AGENT (CURRICULUM PLANNING & WORKLOAD MITIGATION)
# =========================================================================
with tab1:
    st.subheader("Pedagogical Task-Agent: Automated Instructional Scaffolding")
    st.caption("Leverages specialized RAG architecture to automate standard curriculum structures and eliminate repetitive administrative drafting.")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        tier = st.selectbox("Educational Tier & Standard:", [
            "Primary Education (Grade 4) - Foundational Literacy",
            "Lower Secondary (Grade 7) - Integrated Natural Sciences", 
            "Upper Secondary (Grade 11) - Specialized Physics/Chemistry"
        ])
        subject = st.selectbox("Academic Discipline:", ["Natural Sciences", "Mathematics", "Literature", "History & Geography"])
        topic = st.text_input("Lesson Topic:", value="Thermal Expansion of Solids")
        duration = st.slider("Planned Duration (Periods):", 1, 4, 2)
        btn_gen = st.button("🚀 Generate Standardized Lesson Scaffold")
        
    with col2:
        if btn_gen:
            with st.spinner("Querying Local Vector DB (Qdrant) and structuring instructional outcomes..."):
                time.sleep(1.2)
            st.success("Instructional plan generated successfully!")
            
            st.markdown(f"""
            ### INSTRUCTIONAL PLAN: {topic.upper()}
            **Discipline:** {subject} | **Allocated Duration:** {duration} Period(s) | **Target Cohort:** {tier}
            
            #### I. MEASURABLE LEARNING OUTCOMES
            * **Scientific Competence:** Identify, describe, and demonstrate the volumetric expansion of solids under thermal fluctuations.
            * **Inquiry Skills:** Formulate empirical hypotheses regarding differing expansion rates across distinct metallic substances.
            * **Pedagogical Values:** Foster cooperative learning, experimental safety, and structured analytical reporting.
            
            #### II. FOUR-STAGE INSTRUCTIONAL SEQUENCE (Official Curriculum Standard):
            1. **Stage 1: Engagement / Cognitive Activation (7 minutes)**
               - *Objective:* Introduce cognitive dissonance via physical demonstrations (brass sphere and ring test).
               - *Assessment:* Diagnostic qualitative polling.
            2. **Stage 2: Knowledge Construction / Empirical Exploration (20 minutes)**
               - *Objective:* Measure comparative longitudinal expansion across Aluminum, Copper, and Iron bars.
               - *Deliverable:* Collaborative experimental log and comparative dilation graph.
            3. **Stage 3: Practice & Guided Application (10 minutes)**
               - *Content:* Guided problem-solving worksheet addressing railway thermal gap engineering.
            4. **Stage 4: Extension & Real-World Synthesis (8 minutes)**
               - *Content:* Reverse-engineering bimetallic strips utilized in household thermal circuit breakers.
            """)
            
            st.info("💡 **Ergonomic Workload Audit:** Task-Agent compressed preparation duration by approximately **135 minutes**, directly dampening administrative techno-overload.")

# =========================================================================
# TAB 2: BOUNDARY-GUARDIAN (RIGHT TO DISCONNECT FIREWALL)
# =========================================================================
with tab2:
    st.subheader("Boundary-Guardian: Statutory Digital Firewall")
    st.caption("Policy-as-Code engine implementing the Right-to-Disconnect via NLP intent classification and asynchronous triage.")
    
    col_t1, col_t2 = st.columns([1, 1])
    with col_t1:
        sim_hour = st.slider("Simulate Timestamp of Incoming Communication (24-Hour Clock):", 0, 23, 20)
        sender_name = st.text_input("Sender Entity:", value="Parent of Student John Doe (Class 7A)")
        incoming_msg = st.text_area("Incoming Message Payload:", 
                                    value="Good evening, my child cannot solve Question 4 on page 52. Can you please explain it in detail right now?")
        btn_receive = st.button("📩 Simulate Inbound Transmission")
        
    with col_t2:
        if btn_receive:
            # Emergency NLP keyword triage
            emergency_keywords = ["emergency", "hospital", "accident", "injury", "fracture", "ambulance", "bleeding"]
            is_emergency = any(kw in incoming_msg.lower() for kw in emergency_keywords)
            
            if is_emergency:
                st.error("🚨 **CRITICAL OVERRIDE: EMERGENCY PROTOCOL ACTIVATED**")
                st.markdown("""
                * **NLP Triage Classification:** High-risk student safety/medical anomaly detected.
                * **Action:** Bypasses quiet-hour filters immediately. Automated voice dispatch routed to **Campus Security / School Duty Administrator** with simultaneous urgent push alerts to the educator.
                """)
            elif sim_hour >= 18 or sim_hour < 7:
                st.warning(f"🌙 **QUIET-HOURS SHIELD ENGAGED ({sim_hour}:00 - Contracted Rest Interval)**")
                st.markdown(f"""
                * **Educator Terminal Status:** Suppressing 100% of mobile push notifications; zero audible alerts.
                * **Data Buffer:** Transmission securely held in the **07:15 Morning Digest Queue**.
                * **Automated Courteous Dispatch Sent to Originator:**
                > *"Greetings, {sender_name}. The Sentient-EduCore system has successfully buffered your inquiry. As this message arrived outside official contractual hours, the educator will review and address it during standard operational windows (commencing 07:15 tomorrow). Thank you for respecting educational restorative boundaries."*
                """)
            else:
                st.success(f"☀️ **OFFICIAL OPERATIONAL WINDOW ({sim_hour}:00)**")
                st.markdown(f"* Message from {sender_name} seamlessly delivered to the educator's primary Moodle Communications Inbox.")

# =========================================================================
# TAB 3: AFFECTIVE TELEMETRY & CONTEXT-AWARE MICRO-CBT
# =========================================================================
with tab3:
    st.subheader("Affective Telemetry & In-Situ Micro-Interventions")
    st.caption("Passive behavioral telemetry monitoring continuous midnight session length and typing friction without invasive surveillance.")
    
    col_a1, col_a2 = st.columns([1, 1])
    with col_a1:
        st.markdown("**Simulate Active Educator Grading Session on LMS:**")
        session_time = st.selectbox("Continuous Active Interaction Duration:", ["45 Minutes (Baseline)", "1 Hour 30 Minutes", "3 Hours 45 Minutes (Threshold Exceeded)"])
        clock_time = st.selectbox("Current System Chronological Timestamp:", ["14:30 (Daytime)", "20:15 (Evening)", "23:50 (Late-Night / Nocturnal)"])
        typing_stress = st.checkbox("Simulate High-Friction Keystroke Cadence (Rapid Backspace, Erratic Rhythm)", value=True)
        btn_trigger = st.button("⚡ Execute Telemetry Inference Engine")
        
    with col_a2:
        if btn_trigger:
            if "3 Hours 45 Minutes" in session_time and "23:50" in clock_time:
                st.error("⚠️ **TELEMETRY ANOMALY: SEVERE COGNITIVE EXHAUSTION DETECTED**")
                st.markdown("""
                * **Telemetry Correlates:** Sustained continuous activity exceeding 3.5 hours within the circadian nadir ($>23:00$); elevated backspace friction indicates affective distress.
                * **Preservation Action:** Automatic background data checkpoint executed. All grades, rubrics, and draft feedback safely synchronized.
                """)
                
                # Contextual In-Situ CBT Modal
                st.markdown("""
                <div class="cbt-box">
                    <h4 style="color:#BE185D; margin-top:0;">🛑 Affective In-Situ Pause (Micro-CBT Prompt)</h4>
                    <p style="color:#374151; font-size:14px;">
                    <em>"Dear Educator, our telemetry indicates continuous grading activity for nearly 4 hours tonight. 
                    All your input has been securely saved to the persistence vault. 
                    Your cognitive and physiological health takes precedence over late-night compliance. Please pause and reset with a 60-second vagal stimulation exercise."</em>
                    </p>
                    <p><strong>Box Breathing Technique (4-4-4-4 Cadence):</strong></p>
                    <ol>
                        <li>Inhale deeply through your nose for 4 seconds.</li>
                        <li>Retain the breath with relaxed abdominal muscles for 4 seconds.</li>
                        <li>Exhale smoothly through your mouth for 4 seconds.</li>
                        <li>Pause in calm emptiness for 4 seconds.</li>
                    </ol>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.success("✅ **Telemetry Within Nominal Parameters:** Interaction load remains within acceptable cognitive ergonomic bounds.")

# =========================================================================
# TAB 4: POLICY DASHBOARD (EXECUTIVE VIEW WITH DIFFERENTIAL PRIVACY)
# =========================================================================
with tab4:
    st.subheader("Organizational Health Dashboard (Institutional Administration)")
    st.caption("Enforces strict mathematical k-anonymity (k >= 10) to visualize faculty-level burnout risks while protecting individual privacy.")
    
    # Synthetic multi-department dataset
    dept_data = pd.DataFrame({
        "Academic Department": ["Early Childhood Division", "Natural Sciences Faculty", "Humanities & Literature", "Mathematics & CS", "Foreign Languages"],
        "Administrative Workload Ratio (% Cap)": [148, 136, 118, 102, 94],
        "Emotional Exhaustion Score (MBI-EE)": [4.7, 4.3, 3.8, 3.2, 2.8],
        "Nocturnal System Engagement (>22:00) (%)": [82, 68, 54, 35, 20]
    })
    
    st.dataframe(dept_data.style.highlight_max(axis=0, color="#FECACA"), use_container_width=True)
    
    # Plotly Heatmap / Comparative Bar Chart
    fig = px.bar(
        dept_data, 
        x="Academic Department", 
        y="Administrative Workload Ratio (% Cap)", 
        color="Emotional Exhaustion Score (MBI-EE)",
        color_continuous_scale="Reds",
        title="Institutional Stress Heatmap: Faculty Administrative Overload vs. Burnout Indicators"
    )
    fig.add_hline(y=100, line_dash="dash", line_color="blue", annotation_text="Statutory Overtime Threshold (100% Contracted Cap)")
    st.plotly_chart(fig, use_container_width=True)
    
    st.warning("""
    🚨 **INSTITUTIONAL STRATEGIC ADVISORY:**
    * **Early Childhood Division & Natural Sciences Faculty** have breached statutory safety thresholds ($>130\%$ administrative load).
    * **Policy Recommendation:** Executive leadership should eliminate duplicated paper compliance registries, authorize additional teaching assistant allocations, and trigger overtime compensation frameworks in compliance with labor regulations.
    """)
