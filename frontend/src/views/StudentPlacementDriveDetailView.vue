<template>
  <div class="drive-detail-page">

    <div class="topbar">
      <button class="btn-back" @click="$router.back()">← Back</button>
      <div>
        <h1>{{ drive.job_title }}</h1>
        <p>{{ drive.company?.name || 'Company Name' }}</p>
      </div>
    </div>

    <div class="detail-grid">

      <div class="main-content">

        <div class="info-card">
          <h3>Job Description</h3>
          <p class="description">{{ drive.job_description }}</p>
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

        <div class="sidebar-card">
          <h3>Drive Information</h3>
          
          <div class="info-row">
            <span class="label">Company</span>
            <span class="value">{{ drive.company?.name || '—' }}</span>
          </div>
          <div class="info-row">
            <span class="label">Package</span>
            <span class="value highlight">{{ drive.salary || 'Not Disclosed' }}</span>
          </div>
          <div class="info-row">
            <span class="label">Start Date</span>
            <span class="value">{{ drive.start_date }}</span>
          </div>
          <div class="info-row">
            <span class="label">Last Date</span>
            <span class="value deadline">{{ drive.last_date }}</span>
          </div>
          <div class="info-row">
            <span class="label">Status</span>
            <span :class="getStatusClass(drive.status)" class="status-badge">
              {{ drive.status }}
            </span>
          </div>
        </div>

        <div class="sidebar-card">
          <h3>Company Details</h3>
          <div class="info-row">
            <span class="label">Website</span>
            <a :href="drive.company?.website_link" target="_blank" class="value link">
              {{ drive.company?.website_link || 'Not Available' }}
            </a>
          </div>
        </div>

        <button 
          class="btn-apply"
          :disabled="isApplied"
          @click="applyForDrive"
        >
          {{ isApplied ? 'Already Applied' : 'Apply Now' }}
        </button>

      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "StudentDriveDetail",

  data() {
    return {
      drive: {
        id: 1,
        job_title: "Software Engineer",
        job_description: "We are looking for a passionate Software Engineer with strong problem-solving skills and experience in full-stack development.",
        salary: "45 LPA",
        start_date: "25 May 2026",
        last_date: "10 June 2026",
        skills_required: "Python, Django, React, PostgreSQL, AWS, Docker",
        status: "Ongoing",
        company: {
          name: "Google",
          website_link: "https://google.com"
        }
      },
      isApplied: false   
    }
  },

  computed: {
    skillsArray() {
      return this.drive.skills_required ? 
        this.drive.skills_required.split(',').map(s => s.trim()) : []
    }
  },

  methods: {
    getStatusClass(status) {
      if (status === 'Ongoing') return 'badge-ongoing'
      if (status === 'Upcoming') return 'badge-upcoming'
      return 'badge-completed'
    },

    applyForDrive() {
      if (this.isApplied) return
      if (confirm("Are you sure you want to apply for this drive?")) {
        this.isApplied = true
        alert("Application submitted successfully!")
      }
    }
  }
}
</script>

<style scoped>
.drive-detail-page {
  padding: 20px 24px;
}

.topbar {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 30px;
}

.btn-back {
  background: none;
  border: none;
  color: #2563eb;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}

.topbar h1 {
  font-size: 32px;
  color: #111827;
  margin: 0;
}

.topbar p {
  color: #6b7280;
  font-size: 15px;
  margin: 4px 0 0 0;
}

.detail-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
}

.info-card, .sidebar-card {
  background: white;
  border-radius: 18px;
  padding: 24px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  margin-bottom: 20px;
}

.info-card h3, .sidebar-card h3 {
  font-size: 18px;
  color: #111827;
  margin-bottom: 16px;
}

.description {
  line-height: 1.7;
  color: #374151;
  font-size: 15px;
}

.skills-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.skill-tag {
  background: #f1f5f9;
  color: #1e40af;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
}

.info-row {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  border-bottom: 1px solid #f3f4f6;
}

.info-row:last-child {
  border-bottom: none;
}

.label {
  color: #6b7280;
  font-weight: 500;
}

.value {
  font-weight: 600;
  color: #111827;
}

.highlight {
  color: #1e40af;
}

.deadline {
  color: #dc2626;
  font-weight: 600;
}

.link {
  color: #2563eb;
  text-decoration: none;
}

.link:hover {
  text-decoration: underline;
}

.status-badge {
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 13.5px;
  font-weight: 600;
}

.badge-ongoing { background: #fef9c3; color: #ca8a04; }
.badge-upcoming { background: #dbeafe; color: #2563eb; }
.badge-completed { background: #dcfce7; color: #16a34a; }

.btn-apply {
  width: 100%;
  padding: 14px;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 10px;
}

.btn-apply:disabled {
  background: #9ca3af;
  cursor: not-allowed;
}
</style>