<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Complete Profile</h1>
        <p>Fill your details to unlock full features and start applying</p>
      </div>
    </div>

    <div class="profile-grid">

      <div class="section-box preview-box">
        <div class="profile-top">
          <div class="profile-avatar">{{ form.name ? form.name.charAt(0) : '?' }}</div>
          <h2>{{ form.name || 'Your Name' }}</h2>
          <p>{{ form.username ? '@' + form.username : '@username' }}</p>
        </div>

        <div class="preview-details">
          <div class="detail-row">
            <span class="detail-label">Email</span>
            <span class="detail-value">{{ form.email || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">College</span>
            <span class="detail-value">{{ form.college || '—' }}</span>
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
            <span class="detail-label">Status</span>
            <span class="detail-value">{{ form.status || '—' }}</span>
          </div>
        </div>
      </div>

      <div class="section-box form-box">

        <h3 class="form-title">Personal Information</h3>

        <div class="form-row">
          <div class="form-group">
            <label>Full Name <span class="required">*</span></label>
            <input v-model="form.name" type="text" placeholder="Rahul Sharma" />
          </div>
          <div class="form-group">
            <label>Username <span class="required">*</span></label>
            <input v-model="form.username" type="text" placeholder="rahul_sharma" />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Email <span class="required">*</span></label>
            <input v-model="form.email" type="email" placeholder="rahul@college.com" />
          </div>
          <div class="form-group">
            <label>CGPA <span class="required">*</span></label>
            <input v-model="form.cgpa" type="text" placeholder="8.7" />
          </div>
        </div>

        <div class="form-group full">
          <label>College Name <span class="required">*</span></label>
          <input v-model="form.college" type="text" placeholder="IIT Delhi / ABC Engineering College" />
        </div>

        <div class="form-group full">
          <label>Skills <span class="required">*</span></label>
          <input v-model="form.skills" type="text" placeholder="Vue.js, Python, Java, React, Node.js" />
        </div>

        <div class="form-group full">
          <label>Bio / About Yourself</label>
          <textarea v-model="form.bio" placeholder="Write something about yourself..." rows="4"></textarea>
        </div>

        <div class="form-group full">
          <label>Resume (PDF) <span class="required">*</span></label>
          <input type="file" accept=".pdf" class="file-input" @change="handleResumeUpload" />
        </div>

        <div class="form-bottom">
          <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
          <p v-if="successMsg" class="success-msg">✅ Profile Updated Successfully!</p>
          <button class="btn-save" @click="saveProfile">Save & Continue</button>
        </div>

      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "StudentCompleteProfile",

  data() {
    return {
      errorMsg: "",
      successMsg: false,
      form: {
        name: "",
        username: "",
        email: "",
        college: "",
        cgpa: "",
        skills: "",
        bio: "",
        resume: null
      }
    }
  },

  methods: {
    handleResumeUpload(e) {
      this.form.resume = e.target.files[0]
    },

    saveProfile() {
      if (!this.form.name || !this.form.username || !this.form.email || 
          !this.form.college || !this.form.cgpa || !this.form.skills) {
        this.errorMsg = "Please fill all required fields!"
        return
      }

      this.errorMsg = ""
      this.successMsg = true

      setTimeout(() => {
        this.successMsg = false
      }, 3000)

      console.log("Profile Data:", this.form)
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
  gap: 24px;
}

.section-box {
  background: white;
  border-radius: 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  padding: 28px;
}

.preview-box {
  text-align: center;
}

.profile-top {
  margin-bottom: 24px;
}

.profile-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: #eff6ff;
  color: #2563eb;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 34px;
  font-weight: 700;
  margin: 0 auto 16px;
}

.profile-top h2 {
  font-size: 22px;
  color: #111827;
  margin-bottom: 4px;
}

.college {
  color: #6b7280;
  font-size: 15px;
}

.preview-details {
  text-align: left;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  border-bottom: 1px solid #f3f4f6;
}

.detail-label {
  color: #6b7280;
}

.detail-value {
  font-weight: 600;
  color: #111827;
}

.form-title {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 20px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.form-group {
  margin-bottom: 18px;
}

.form-group.full {
  grid-column: span 2;
}

.form-group label {
  display: block;
  margin-bottom: 6px;
  font-weight: 600;
  color: #374151;
  font-size: 14px;
}

.required {
  color: #dc2626;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 11px 14px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  font-size: 15px;
  outline: none;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #2563eb;
}

.file-input {
  width: 100%;
  padding: 8px;
  border: 1px dashed #cbd5e1;
  border-radius: 10px;
  background: #f8fafc;
}

.btn-save {
  width: 100%;
  padding: 13px;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 10px;
}

.btn-save:hover {
  background: #1d4ed8;
}

.success-msg {
  color: #16a34a;
  font-weight: 600;
  text-align: center;
  margin: 10px 0;
}

.error-msg {
  color: #dc2626;
  font-weight: 600;
  text-align: center;
  margin: 10px 0;
}
</style>