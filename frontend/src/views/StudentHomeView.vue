<template>
  <div>

    <div class="topbar">
      <h1>Student Dashboard</h1>
    </div>

    <div class="cards">
      <div class="card">
        <h2>{{ appliedJobs }}</h2>
        <p>Applied Jobs</p>
      </div>
      <div class="card">
        <h2>{{ selectedJobs }}</h2>
        <p>Selected</p>
      </div>
      <div class="card">
        <h2>{{ pendingJobs }}</h2>
        <p>Pending</p>
      </div>
      <div class="card">
        <h2>{{ upcomingDrives }}</h2>
        <p>Upcoming Drives</p>
      </div>
    </div>

    <div class="requests-grid">

      <div class="section-box">
        <div class="section-header">
          <h3>My Recent Applications</h3>
        </div>

        <div v-if="applications.length === 0" class="empty">
          No applications yet
        </div>

        <div
          v-for="app in applications.slice(0, 5)"
          :key="app.id"
          class="request-item"
        >
          <div class="request-left">
            <div class="avatar">{{ app.company.charAt(0) }}</div>
            <div>
              <p class="request-name">{{ app.company }}</p>
              <p class="request-sub">{{ app.role }} · {{ app.appliedOn }}</p>
            </div>
          </div>
          <span :class="
            app.status === 'Selected' ? 'badge-selected' :
            app.status === 'Pending'  ? 'badge-pending'  :
            'badge-rejected'
          ">{{ app.status }}</span>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header">
          <h3>Upcoming Drives</h3>
        </div>

        <div v-if="drives.length === 0" class="empty">
          No upcoming drives
        </div>

        <div
          v-for="drive in drives.slice(0, 5)"
          :key="drive.id"
          class="request-item"
        >
          <div class="request-left">
            <div class="avatar">{{ drive.company.charAt(0) }}</div>
            <div>
              <p class="request-name">{{ drive.company }}</p>
              <p class="request-sub">{{ drive.role }} · {{ drive.date }}</p>
            </div>
          </div>
          <span class="badge-upcoming">{{ drive.package }}</span>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "StudentHomeView",

  data() {
    return {
      applications: [
        { id: 1, company: "Google",    role: "Software Engineer",    appliedOn: "10 May 2026", status: "Selected" },
        { id: 2, company: "Microsoft", role: "SDE-1",                appliedOn: "11 May 2026", status: "Pending"  },
        { id: 3, company: "Amazon",    role: "Backend Developer",    appliedOn: "12 May 2026", status: "Rejected" },
        { id: 4, company: "Flipkart",  role: "Frontend Developer",   appliedOn: "13 May 2026", status: "Pending"  },
        { id: 5, company: "Zomato",    role: "Full Stack Developer",  appliedOn: "14 May 2026", status: "Selected" },
      ],
      drives: [
        { id: 1, company: "Google",    role: "Software Engineer",   date: "25 May 2026", package: "45 LPA" },
        { id: 2, company: "Microsoft", role: "SDE-1",               date: "28 May 2026", package: "40 LPA" },
        { id: 3, company: "Flipkart",  role: "Frontend Developer",  date: "30 May 2026", package: "28 LPA" },
        { id: 4, company: "Infosys",   role: "Systems Engineer",    date: "02 Jun 2026", package: "8 LPA"  },
        { id: 5, company: "Wipro",     role: "Junior Developer",    date: "05 Jun 2026", package: "6 LPA"  },
      ]
    }
  },

  computed: {
    appliedJobs()    { return this.applications.length },
    selectedJobs()   { return this.applications.filter(a => a.status === 'Selected').length },
    pendingJobs()    { return this.applications.filter(a => a.status === 'Pending').length },
    upcomingDrives() { return this.drives.length }
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

.badge-pending {
  background: #fef9c3;
  color: #ca8a04;
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