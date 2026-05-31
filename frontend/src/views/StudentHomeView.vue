<template>
  <div>

    <div class="topbar">
      <h1>Student Dashboard</h1>
    </div>

    <div v-if="!profileComplete" class="profile-banner">
      <div class="banner-left">
        <span class="banner-icon">⚠️</span>
        <div>
          <p class="banner-title">Complete Your Profile First!</p>
          <p class="banner-sub">Please complete your profile before applying for a drive.</p>
        </div>
      </div>
      <button class="btn-complete" @click="goToProfile">Complete Profile</button>
    </div>

    <div v-if="loadingStats" class="empty" style="padding: 40px 0;">
      Loading...
    </div>

    <div v-else class="cards">
      <div class="card">
        <h2>{{ stats.total_applications }}</h2>
        <p>Total Applications</p>
      </div>
      <div class="card">
        <h2>{{ stats.shortlisted }}</h2>
        <p>Shortlisted</p>
      </div>
      <div class="card">
        <h2>{{ stats.selected }}</h2>
        <p>Selected</p>
      </div>
      <div class="card">
        <h2>{{ stats.ongoing_drives }}</h2>
        <p>Active Drives</p>
      </div>
    </div>

    <div class="requests-grid">

      <div class="section-box">
        <div class="section-header">
          <h3>My Recent Applications</h3>
        </div>

        <div v-if="loadingStats" class="empty">Loading...</div>

        <div v-else-if="applications.length === 0" class="empty">
          No applications yet
        </div>

        <div
          v-for="app in applications.slice(0, 5)"
          :key="app.id"
          class="request-item"
        >
          <div class="request-left">
            <div class="avatar">{{ app.company ? app.company.charAt(0) : '?' }}</div>
            <div>
              <p class="request-name">{{ app.company }}</p>
              <p class="request-sub">{{ app.drive_title }} · {{ app.apply_date }}</p>
            </div>
          </div>
          <span :class="
            app.status === 'Selected'    ? 'badge-selected'    :
            app.status === 'Shortlisted' ? 'badge-shortlisted' :
            app.status === 'Pending'     ? 'badge-pending'     :
            'badge-rejected'
          ">{{ app.status }}</span>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header">
          <h3>Active Drives</h3>
        </div>

        <div v-if="loadingStats" class="empty">Loading...</div>

        <div v-else-if="drives.length === 0" class="empty">
          No active drives
        </div>

        <div
          v-for="drive in drives.slice(0, 5)"
          :key="drive.id"
          class="request-item"
        >
          <div class="request-left">
            <div class="avatar">{{ drive.company ? drive.company.charAt(0) : '?' }}</div>
            <div>
              <p class="request-name">{{ drive.company }}</p>
              <p class="request-sub">{{ drive.job_title }} · {{ drive.end_date }}</p>
            </div>
          </div>
          <span class="badge-upcoming">{{ drive.salary || 'N/A' }}</span>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "StudentHomeView",

  data() {
    return {
      loadingStats:    true,
      profileComplete: true,
      stats: {
        total_applications: 0,
        selected:           0,
        shortlisted:        0,
        ongoing_drives:     0,
      },
      applications: [],
      drives:       [],
    }
  },

  async mounted() {
    await this.fetchDashboardData()
  },

  methods: {

    getHeaders() {
      return {
        headers: {
          "Authentication-Token": localStorage.getItem("token"),
        },
      }
    },

    async fetchDashboardData() {
      this.loadingStats = true
      try {
        const res = await axios.get("http://localhost:5000/student/dashboard_data", this.getHeaders())
        const data = res.data
        this.stats           = Object.assign({}, data.stats)
        this.applications    = data.applications     || []
        this.drives          = data.placement_drives || []
        this.profileComplete = data.profile_complete
      } catch (err) {
        console.error("Dashboard data load failed:", err)
      } finally {
        this.loadingStats = false
      }
    },

    goToProfile() {
      this.$router.push("/student_dashboard/profile")
    }

  }
}
</script>

<style scoped>
.topbar {
  margin-bottom: 30px;
}
.topbar h1 {
  font-size: 34px;
  color: #111827;
}
.profile-banner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fefce8;
  border: 1px solid #fde047;
  border-radius: 14px;
  padding: 18px 24px;
  margin-bottom: 24px;
}
.banner-left {
  display: flex;
  align-items: center;
  gap: 14px;
}
.banner-icon {
  font-size: 24px;
}
.banner-title {
  font-size: 15px;
  font-weight: 700;
  color: #854d0e;
}
.banner-sub {
  font-size: 13px;
  color: #a16207;
  margin-top: 2px;
}
.btn-complete {
  background: #ca8a04;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
}
.btn-complete:hover {
  background: #a16207;
}
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}
.card {
  background: white;
  padding: 24px;
  border-radius: 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}
.card h2 {
  font-size: 30px;
  color: #2563eb;
  margin-bottom: 8px;
  font-weight: 700;
}
.card p {
  color: #6b7280;
  font-size: 14px;
}
.requests-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}
.section-box {
  background: white;
  border-radius: 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  padding: 24px;
}
.section-header {
  margin-bottom: 20px;
}
.section-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}
.request-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 0;
  border-bottom: 1px solid #f3f4f6;
}
.request-item:last-of-type {
  border-bottom: none;
}
.request-left {
  display: flex;
  align-items: center;
  gap: 12px;
}
.avatar {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #eff6ff;
  color: #2563eb;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 15px;
  font-weight: 700;
  flex-shrink: 0;
}
.request-name {
  font-size: 14px;
  font-weight: 600;
  color: #111827;
}
.request-sub {
  font-size: 13px;
  color: #6b7280;
  margin-top: 2px;
}
.badge-selected {
  background: #dcfce7;
  color: #16a34a;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}
.badge-shortlisted {
  background: #fef9c3;
  color: #ca8a04;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}
.badge-pending {
  background: #dbeafe;
  color: #2563eb;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}
.badge-rejected {
  background: #fee2e2;
  color: #dc2626;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}
.badge-upcoming {
  background: #eff6ff;
  color: #2563eb;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  white-space: nowrap;
}
.empty {
  text-align: center;
  color: #9ca3af;
  font-size: 14px;
  padding: 30px 0;
}
</style>