<template>
  <div class="application-detail-page">

    <button class="btn-back" @click="$router.back()">
      ← Back
    </button>

    <div class="header">
      <div>
        <h1>{{ application.drive }}</h1>
        <p class="company">{{ application.company }}</p>
      </div>
      <span :class="getStatusClass(application.status)" class="status-badge">
        {{ application.status }}
      </span>
    </div>

    <div class="detail-grid">

      <div class="main-info">

        <div class="info-card">
          <h3>Drive Information</h3>
          <div class="info-row">
            <span class="label">Package</span>
            <span class="value">{{ application.package }}</span>
          </div>
          <div class="info-row">
            <span class="label">Start Date</span>
            <span class="value">{{ application.start_date }}</span>
          </div>
          <div class="info-row">
            <span class="label">Last Date</span>
            <span class="value deadline">{{ application.last_date }}</span>
          </div>
          <div class="info-row">
            <span class="label">Applied On</span>
            <span class="value">{{ application.applied_on }}</span>
          </div>
        </div>

        <div class="info-card">
          <h3>Required Skills</h3>
          <div class="skills-list">
            <span v-for="(skill, i) in skillsArray" :key="i" class="skill-tag">
              {{ skill }}
            </span>
          </div>
        </div>

      </div>

      <div class="sidebar">

        <div class="info-card">
          <h3>Your Application Details</h3>
          
          <div class="info-row">
            <span class="label">Status</span>
            <span :class="getStatusClass(application.status)" class="status-badge">
              {{ application.status }}
            </span>
          </div>
          <div class="info-row">
            <span class="label">Your Resume</span>
            <a :href="application.resume" target="_blank" class="resume-link">
              View Resume →
            </a>
          </div>
        </div>

        <div v-if="application.interview_date" class="info-card">
          <h3>Interview Details</h3>
          <div class="info-row">
            <span class="label">Interview Date</span>
            <span class="value">{{ application.interview_date }}</span>
          </div>
          <div class="info-row">
            <span class="label">Mode</span>
            <span class="value">{{ application.interview_mode }}</span>
          </div>
        </div>

        <button class="btn-withdraw" v-if="application.status === 'Applied'" @click="withdrawApplication">
          Withdraw Application
        </button>

      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "StudentApplicationDetail",

  data() {
    return {
      application: {
        id: 1,
        drive: "Software Engineer Hiring",
        company: "Google",
        package: "45 LPA",
        start_date: "25 May 2026",
        last_date: "10 June 2026",
        applied_on: "20 May 2026",
        status: "Shortlisted",
        resume: "#",
        skills: "Python, Django, React, AWS, Docker",
        interview_date: "05 June 2026",
        interview_mode: "Online (Google Meet)"
      }
    }
  },

  computed: {
    skillsArray() {
      return this.application.skills ? 
        this.application.skills.split(',').map(s => s.trim()) : []
    }
  },

  methods: {
    getStatusClass(status) {
      if (status === 'Selected') return 'badge-selected'
      if (status === 'Shortlisted') return 'badge-shortlisted'
      if (status === 'Rejected') return 'badge-rejected'
      return 'badge-applied'
    },

    withdrawApplication() {
      if (confirm("Are you sure you want to withdraw this application?")) {
        alert("Application withdrawn successfully.")
      }
    }
  }
}
</script>

<style scoped>
.application-detail-page {
  padding: 20px 28px;
  max-width: 1100px;
  margin: 0 auto;
}

.btn-back {
  background: none;
  border: none;
  color: #2563eb;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
}

.header h1 {
  font-size: 30px;
  color: #0f172a;
  margin: 0;
}

.company {
  font-size: 17px;
  color: #475569;
  margin-top: 6px;
}

.detail-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 28px;
}

.info-card {
  background: white;
  border-radius: 18px;
  padding: 26px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
  margin-bottom: 20px;
}

.info-card h3 {
  font-size: 19px;
  color: #111827;
  margin-bottom: 18px;
}

.info-row {
  display: flex;
  justify-content: space-between;
  padding: 13px 0;
  border-bottom: 1px solid #f1f5f9;
}

.info-row:last-child {
  border-bottom: none;
}

.label {
  color: #64748b;
}

.value {
  font-weight: 600;
  color: #1e2937;
}

.deadline {
  color: #e11d48;
}

.skills-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.skill-tag {
  background: #f1f5f9;
  color: #1e40af;
  padding: 8px 16px;
  border-radius: 30px;
  font-size: 14px;
}

.resume-link {
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
}

.resume-link:hover {
  text-decoration: underline;
}

.btn-withdraw {
  width: 100%;
  padding: 12px;
  background: #fee2e2;
  color: #dc2626;
  border: none;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}

.status-badge {
  padding: 8px 16px;
  border-radius: 30px;
  font-size: 14px;
  font-weight: 600;
}

.badge-applied     { background: #dbeafe; color: #2563eb; }
.badge-shortlisted { background: #fef3c7; color: #ca8a04; }
.badge-rejected    { background: #fee2e2; color: #dc2626; }
.badge-selected    { background: #dcfce7; color: #16a34a; }
</style>