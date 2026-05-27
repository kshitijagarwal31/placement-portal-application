<template>

  <div class="home">

    <Navbar />

    <main class="main-content">

      <section class="hero">

        <div class="hero-left">

          <p class="hero-small-text">
            SMART COLLEGE PLACEMENT PLATFORM
          </p>

          <h1>
            Connecting Students <br />
            With Top Companies
          </h1>

          <p class="hero-description">
            PlaceMe helps students discover opportunities, apply for jobs,
            track applications and connect with leading companies from one platform.
          </p>

          <div class="hero-buttons">

            <router-link to="/register" class="primary-btn">
              Get Started
            </router-link>

            <router-link to="/login" class="secondary-btn">
              Sign In
            </router-link>

          </div>

        </div>

        <div class="hero-right">

          <div class="dashboard-card">

            <div class="dashboard-top">

              <h3>
                Placement Overview
              </h3>

              <span class="live-badge">
                Live
              </span>

            </div>

            <div class="stats-grid">

              <div class="stat-box">
                <h2>500+</h2>
                <p>Companies</p>
              </div>

              <div class="stat-box">
                <h2>10K+</h2>
                <p>Students</p>
              </div>

              <div class="stat-box">
                <h2>95%</h2>
                <p>Placement</p>
              </div>

              <div class="stat-box">
                <h2>1.2K+</h2>
                <p>Job Posts</p>
              </div>

            </div>

          </div>

        </div>

      </section>

      <section class="features-section">

        <div class="section-heading">

          <h2>
            Why Choose PlaceMe?
          </h2>

          <p>
            Everything required to manage placements efficiently.
          </p>

        </div>

        <div class="features-grid">

          <div class="feature-card">

            <div class="feature-icon">
              🎓
            </div>

            <h3>
              Student Profiles
            </h3>

            <p>
              Create profiles, upload resumes and manage placement details.
            </p>

          </div>

          <div class="feature-card">

            <div class="feature-icon">
              🏢
            </div>

            <h3>
              Company Access
            </h3>

            <p>
              Companies can post jobs and shortlist candidates easily.
            </p>

          </div>

          <div class="feature-card">

            <div class="feature-icon">
              📄
            </div>

            <h3>
              Easy Applications
            </h3>

            <p>
              Apply to internships and jobs in just a few clicks.
            </p>

          </div>

          <div class="feature-card">

            <div class="feature-icon">
              📊
            </div>

            <h3>
              Placement Tracking
            </h3>

            <p>
              Monitor applications, interviews and placement status.
            </p>

          </div>

        </div>

      </section>

    </main>

    <footer class="footer">

      <p>
        © 2026 PlaceMe Portal. All Rights Reserved.
      </p>

    </footer>

  </div>

</template>

<script>

import Navbar from "../components/Navbar.vue"

export default {
  name: "HomeView",
  components:{
    Navbar
  }
}

</script>

<style scoped>

.home{
  min-height:100vh;
  background:#f5f7fb;
  color:#111827;
  display:flex;
  flex-direction:column;
}

.main-content{
  flex:1;
}

.hero{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:80px 60px;
  gap:40px;
}

.hero-left{
  flex:1;
}

.hero-small-text{
  color:#2563eb;
  font-size:14px;
  font-weight:bold;
  margin-bottom:18px;
  letter-spacing:1px;
}

.hero-left h1{
  font-size:58px;
  line-height:1.2;
  margin-bottom:22px;
}

.hero-description{
  color:#6b7280;
  font-size:18px;
  line-height:1.8;
  max-width:650px;
  margin-bottom:35px;
}

.hero-buttons{
  display:flex;
  gap:16px;
}

.primary-btn{
  text-decoration:none;
  background:#2563eb;
  color:white;
  padding:14px 28px;
  border-radius:10px;
  font-weight:bold;
  transition:0.2s;
}

.primary-btn:hover{
  background:#1d4ed8;
}

.secondary-btn{
  text-decoration:none;
  border:2px solid #2563eb;
  color:#2563eb;
  padding:14px 28px;
  border-radius:10px;
  font-weight:bold;
  transition:0.2s;
}

.secondary-btn:hover{
  background:#2563eb;
  color:white;
}

.hero-right{
  flex:1;
  display:flex;
  justify-content:center;
}

.dashboard-card{
  width:100%;
  max-width:420px;
  background:white;
  border-radius:20px;
  padding:30px;
  box-shadow:0 10px 35px rgba(0,0,0,0.08);
}

.dashboard-top{
  display:flex;
  justify-content:space-between;
  align-items:center;
  margin-bottom:25px;
}

.dashboard-top h3{
  font-size:22px;
}

.live-badge{
  background:#dcfce7;
  color:#16a34a;
  padding:6px 12px;
  border-radius:20px;
  font-size:13px;
  font-weight:bold;
}

.stats-grid{
  display:grid;
  grid-template-columns:repeat(2,1fr);
  gap:16px;
}

.stat-box{
  background:#f9fafb;
  border-radius:14px;
  padding:24px 16px;
  text-align:center;
}

.stat-box h2{
  color:#2563eb;
  font-size:30px;
  margin-bottom:8px;
}

.stat-box p{
  color:#6b7280;
  font-weight:bold;
  font-size:14px;
}

.features-section{
  padding:20px 60px 80px;
}

.section-heading{
  text-align:center;
  margin-bottom:45px;
}

.section-heading h2{
  font-size:40px;
  margin-bottom:10px;
}

.section-heading p{
  color:#6b7280;
}

.features-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:22px;
}

.feature-card{
  background:white;
  padding:30px 24px;
  border-radius:18px;
  text-align:center;
  box-shadow:0 3px 15px rgba(0,0,0,0.05);
  transition:0.2s;
}

.feature-card:hover{
  transform:translateY(-4px);
}

.feature-icon{
  font-size:44px;
  margin-bottom:18px;
}

.feature-card h3{
  margin-bottom:12px;
  font-size:22px;
}

.feature-card p{
  color:#6b7280;
  line-height:1.7;
}

.footer{
  text-align:center;
  padding:24px;
  border-top:1px solid #e5e7eb;
  color:#6b7280;
  background:white;
}

</style>