<template>
  <div>

    <button class="btn-back" @click="$router.back()">← Back</button>

    <div class="profile-box">

      <div class="profile-header">
        <div class="avatar">{{ application.student_name.charAt(0) }}</div>
        <div>
          <h1>{{ application.student_name }}</h1>
          <p>{{ application.student_email }}</p>
        </div>
        <span :class="
          application.status === 'Pending'  ? 'badge-pending'  :
          application.status === 'Selected' ? 'badge-selected' :
          'badge-rejected'
        ">{{ application.status }}</span>
      </div>

      <p class="section-label">Placement Drive</p>
      <div class="info-grid">
        <div class="info-item">
          <p class="info-label">Job Title</p>
          <p class="info-value">{{ application.drive_title }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Company</p>
          <p class="info-value">{{ application.company }}</p>
        </div>
      </div>

      <p class="section-label">Application Details</p>
      <div class="info-grid">
        <div class="info-item">
          <p class="info-label">Apply Date</p>
          <p class="info-value">{{ application.apply_date }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Status</p>
          <p class="info-value">
            <span :class="
              application.status === 'Pending'  ? 'badge-pending'  :
              application.status === 'Selected' ? 'badge-selected' :
              'badge-rejected'
            ">{{ application.status }}</span>
          </p>
        </div>
        <div class="info-item">
          <p class="info-label">Interview Date</p>
          <p class="info-value">{{ application.interview_date || '—' }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Interview Mode</p>
          <p class="info-value">{{ application.interview_mode || '—' }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Interview Location</p>
          <p class="info-value">{{ application.interview_location || '—' }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Offer Letter</p>
          <p class="info-value">
            <a v-if="application.offer_letter" :href="application.offer_letter" class="link" target="_blank">📩 View</a>
            <span v-else>—</span>
          </p>
        </div>
      </div>

      <p class="section-label">Feedback</p>
      <div class="feedback-box">
        {{ application.feedback || 'No feedback provided.' }}
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "AdminApplicationDetailView",

  data() {
    return {
      application: {
        id: 1,
        student_name: "Rahul Sharma",
        student_email: "rahul@example.com",
        drive_title: "Software Engineer",
        company: "Google",
        apply_date: "10 May 2026",
        status: "Selected",
        interview_date: "20 May 2026, 10:00 AM",
        interview_mode: "Online",
        interview_location: "Google Meet",
        feedback: "Strong problem-solving skills. Excellent DSA knowledge.",
        offer_letter: "/files/offer_letter_rahul.pdf",
      }
    }
  }
}
</script>

<style scoped>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.btn-back {
  background: none;
  border: none;
  color: #2563eb;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 20px;
  padding: 0;
}
.btn-back:hover { text-decoration: underline; }

.profile-box {
  background: white;
  border-radius: 18px;
  padding: 28px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 28px;
  padding-bottom: 22px;
  border-bottom: 1px solid #f3f4f6;
}

.avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: #eff6ff;
  color: #2563eb;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 22px;
  font-weight: 700;
  flex-shrink: 0;
}

.profile-header h1 {
  font-size: 18px;
  color: #111827;
  font-weight: 600;
  margin-bottom: 4px;
}
.profile-header p {
  font-size: 13px;
  color: #6b7280;
}
.profile-header span { margin-left: auto; }

.section-label {
  font-size: 12px;
  font-weight: 700;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 12px;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 24px;
}

.info-item {
  background: #f9fafb;
  padding: 14px 16px;
  border-radius: 10px;
}

.info-label {
  font-size: 12px;
  color: #6b7280;
  margin-bottom: 6px;
}

.info-value {
  font-size: 14px;
  color: #111827;
  font-weight: 600;
}

.feedback-box {
  background: #f9fafb;
  border-radius: 10px;
  padding: 16px;
  font-size: 14px;
  color: #374151;
  line-height: 1.6;
}

.link {
  color: #2563eb;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
}
.link:hover { text-decoration: underline; }

.badge-pending {
  background: #fef9c3; color: #ca8a04;
  padding: 4px 12px; border-radius: 20px;
  font-size: 12px; font-weight: 600;
}
.badge-selected {
  background: #dcfce7; color: #16a34a;
  padding: 4px 12px; border-radius: 20px;
  font-size: 12px; font-weight: 600;
}
.badge-rejected {
  background: #fee2e2; color: #dc2626;
  padding: 4px 12px; border-radius: 20px;
  font-size: 12px; font-weight: 600;
}

</style>