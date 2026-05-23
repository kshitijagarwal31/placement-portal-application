<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Complete Profile</h1>
        <p>Fill in your details to start applying for jobs</p>
      </div>
    </div>

    <div class="profile-grid">

      <div class="section-box">

        <div class="profile-top">
          <div class="profile-avatar">{{ form.name ? form.name.charAt(0) : '?' }}</div>
          <h2>{{ form.name || 'Your Name' }}</h2>
          <p>{{ form.branch || 'Branch' }} · {{ form.year || 'Year' }}</p>
          <p class="college">{{ form.college || 'College Name' }}</p>
        </div>

        <div class="profile-details">
          <div class="detail-row">
            <span class="detail-label">Email</span>
            <span class="detail-value">{{ form.email || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Phone</span>
            <span class="detail-value">{{ form.phone || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">CGPA</span>
            <span class="detail-value">{{ form.cgpa || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Skills</span>
            <span class="detail-value">{{ form.skills || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">LinkedIn</span>
            <span class="detail-value">{{ form.linkedin || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">GitHub</span>
            <span class="detail-value">{{ form.github || '—' }}</span>
          </div>
        </div>

        <div class="progress-section">
          <div class="progress-header">
            <span class="progress-label">Profile Completion</span>
            <span class="progress-percent">{{ completionPercent }}%</span>
          </div>
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: completionPercent + '%' }"></div>
          </div>
        </div>

      </div>

      <div class="section-box">

        <h3 class="form-title">Your Details</h3>

        <div class="form-row">
          <div class="form-group">
            <label>Full Name <span class="required">*</span></label>
            <input v-model="form.name" type="text" placeholder="Rahul Sharma" />
          </div>
          <div class="form-group">
            <label>Email <span class="required">*</span></label>
            <input v-model="form.email" type="email" placeholder="rahul@college.com" />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Phone <span class="required">*</span></label>
            <input v-model="form.phone" type="text" placeholder="+91 9876543210" />
          </div>
          <div class="form-group">
            <label>CGPA <span class="required">*</span></label>
            <input v-model="form.cgpa" type="text" placeholder="8.5" />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Branch <span class="required">*</span></label>
            <select v-model="form.branch">
              <option value="">Select Branch</option>
              <option>CSE</option>
              <option>ECE</option>
              <option>ME</option>
              <option>EE</option>
              <option>IT</option>
              <option>Civil</option>
            </select>
          </div>
          <div class="form-group">
            <label>Year <span class="required">*</span></label>
            <select v-model="form.year">
              <option value="">Select Year</option>
              <option>1st Year</option>
              <option>2nd Year</option>
              <option>3rd Year</option>
              <option>4th Year</option>
            </select>
          </div>
        </div>

        <div class="form-group full">
          <label>College Name <span class="required">*</span></label>
          <input v-model="form.college" type="text" placeholder="ABC Engineering College" />
        </div>

        <div class="form-group full">
          <label>Skills <span class="required">*</span></label>
          <input v-model="form.skills" type="text" placeholder="e.g. Vue, Python, Java, React" />
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>LinkedIn</label>
            <input v-model="form.linkedin" type="text" placeholder="linkedin.com/in/rahul" />
          </div>
          <div class="form-group">
            <label>GitHub</label>
            <input v-model="form.github" type="text" placeholder="github.com/rahul" />
          </div>
        </div>

        <div class="form-group full">
          <label>About Yourself</label>
          <textarea v-model="form.about" placeholder="Write a short intro about yourself..." rows="3"></textarea>
        </div>

        <div class="form-bottom">
          <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
          <p v-if="saved" class="save-msg">✅ Profile saved successfully!</p>
          <button class="btn-save" @click="saveProfile">Save Profile</button>
        </div>

      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "StudentProfileView",

  data() {
    return {
      saved: false,
      errorMsg: "",
      form: {
        name:     "",
        email:    "",
        phone:    "",
        cgpa:     "",
        branch:   "",
        year:     "",
        college:  "",
        skills:   "",
        linkedin: "",
        github:   "",
        about:    "",
      }
    }
  },

  computed: {
    completionPercent() {
      const fields = ['name', 'email', 'phone', 'cgpa', 'branch', 'year', 'college', 'skills']
      const filled = fields.filter(f => this.form[f] !== '').length
      return Math.round((filled / fields.length) * 100)
    }
  },

  methods: {
    saveProfile() {
      const required = ['name', 'email', 'phone', 'cgpa', 'branch', 'year', 'college', 'skills']
      const allFilled = required.every(f => this.form[f] !== '')

      if (!allFilled) {
        this.errorMsg = "Please fill all required fields!"
        return
      }

      this.errorMsg = ""
      this.saved = true
      setTimeout(() => { this.saved = false }, 3000)
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
  margin-bottom: 5px;
}

.topbar p {
  color: #6b7280;
  font-size: 15px;
}

.profile-grid {
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: 20px;
}

.section-box {
  background: white;
  border-radius: 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  padding: 28px;
}

.profile-top {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-bottom: 24px;
  border-bottom: 1px solid #f3f4f6;
  margin-bottom: 24px;
}

.profile-avatar {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: #eff6ff;
  color: #2563eb;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 30px;
  font-weight: 700;
  margin-bottom: 14px;
}

.profile-top h2 {
  font-size: 20px;
  font-weight: 700;
  color: #111827;
  margin-bottom: 4px;
}

.profile-top p {
  font-size: 14px;
  color: #6b7280;
  margin-bottom: 2px;
}

.college {
  font-size: 13px;
  color: #9ca3af;
}

.profile-details {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 24px;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid #f3f4f6;
}

.detail-label {
  color: #6b7280;
}

.detail-value {
  color: #111827;
  font-weight: 600;
  text-align: right;
  max-width: 60%;
  word-break: break-word;
}

.progress-section {
  margin-top: 8px;
}

.progress-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
}

.progress-label {
  font-size: 13px;
  color: #6b7280;
  font-weight: 500;
}

.progress-percent {
  font-size: 13px;
  font-weight: 700;
  color: #2563eb;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #e5e7eb;
  border-radius: 20px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: #2563eb;
  border-radius: 20px;
  transition: width 0.4s ease;
}

.form-title {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 20px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.form-group {
  margin-bottom: 16px;
}

.form-group.full {
  grid-column: span 2;
}

.form-group label {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 6px;
}

.required {
  color: #dc2626;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 10px 14px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  font-size: 14px;
  color: #111827;
  outline: none;
  transition: 0.2s;
  box-sizing: border-box;
  background: white;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  border-color: #2563eb;
}

.form-bottom {
  margin-top: 4px;
}

.btn-save {
  width: 100%;
  padding: 12px;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-save:hover {
  background: #1d4ed8;
}

.save-msg {
  color: #16a34a;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 10px;
}

.error-msg {
  color: #dc2626;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 10px;
}

</style>