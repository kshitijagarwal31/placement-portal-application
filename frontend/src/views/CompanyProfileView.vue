<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Company Profile</h1>
        <p>Manage your company information</p>
      </div>
    </div>

    <div class="form-grid">

      <div class="section-box">

        <div class="preview-top">
          <div class="preview-avatar">{{ form.full_name ? form.full_name.charAt(0) : '?' }}</div>
          <h2>{{ form.full_name || 'Company Name' }}</h2>
          <p>{{ form.industry || 'Industry' }}</p>
        </div>

        <div class="profile-details">
          <div class="detail-row">
            <span class="detail-label">Username</span>
            <span class="detail-value">{{ form.username || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Email</span>
            <span class="detail-value">{{ form.email || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">HR Contact</span>
            <span class="detail-value">{{ form.hr_contact || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Address</span>
            <span class="detail-value">{{ form.address || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Website</span>
            <span class="detail-value">{{ form.website || '—' }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Account Status</span>
            <span class="badge-active">Active</span>
          </div>
        </div>

        <div class="info-box">
          <p>💡 Keep your profile updated so students can learn more about your company.</p>
        </div>

      </div>

      <div class="section-box">

        <h3 class="form-title">Company Information</h3>

        <div class="form-row">
          <div class="form-group">
            <label>Full Name <span class="required">*</span></label>
            <input v-model="form.full_name" type="text" placeholder="e.g. Google India Pvt Ltd" />
          </div>
          <div class="form-group">
            <label>Username <span class="required">*</span></label>
            <input v-model="form.username" type="text" placeholder="e.g. google_hr" />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Email <span class="required">*</span></label>
            <input v-model="form.email" type="email" placeholder="e.g. hr@google.com" />
          </div>
          <div class="form-group">
            <label>Industry <span class="required">*</span></label>
            <input v-model="form.industry" type="text" placeholder="e.g. Information Technology" />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>HR Contact Number <span class="required">*</span></label>
            <input v-model="form.hr_contact" type="text" placeholder="e.g. +91 9876543210" />
          </div>
          <div class="form-group">
            <label>Website Link</label>
            <input v-model="form.website" type="text" placeholder="e.g. www.google.com" />
          </div>
        </div>

        <div class="form-group">
          <label>Address <span class="required">*</span></label>
          <input v-model="form.address" type="text" placeholder="e.g. 123, MG Road, Bangalore, India" />
        </div>

        <div class="form-group">
          <label>Description</label>
          <textarea v-model="form.description" placeholder="Write a short description about your company..." rows="4"></textarea>
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
  name: "CompanyProfileView",

  data() {
    return {
      saved: false,
      errorMsg: "",
      form: {
        full_name:   "",
        username:    "",
        email:       "",
        industry:    "",
        hr_contact:  "",
        website:     "",
        address:     "",
        description: "",
      }
    }
  },

  methods: {
    saveProfile() {
      const required = ['full_name', 'username', 'email', 'industry', 'hr_contact', 'address']
      const allFilled = required.every(f => this.form[f] !== '')

      if (!allFilled) {
        this.errorMsg = "Please fill all required fields!"
        return
      }

      this.errorMsg = ""
      this.saved    = true

      setTimeout(() => {
        this.saved = false
      }, 3000)
    }
  }
}
</script>

<style scoped>

.topbar {
  margin-bottom: 34px;
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

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1.8fr;
  gap: 24px;
}

.section-box {
  background: white;
  border-radius: 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  padding: 34px;
}

.preview-top {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-bottom: 28px;
  border-bottom: 1px solid #f3f4f6;
  margin-bottom: 28px;
}

.preview-avatar {
  width: 82px;
  height: 82px;
  border-radius: 50%;
  background: #eff6ff;
  color: #2563eb;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 34px;
  font-weight: 700;
  margin-bottom: 16px;
}

.preview-top h2 {
  font-size: 22px;
  font-weight: 700;
  color: #111827;
  margin-bottom: 6px;
}

.preview-top p {
  font-size: 15px;
  color: #6b7280;
}

.profile-details {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 28px;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 15px;
  padding-bottom: 12px;
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

.badge-active {
  background: #dcfce7;
  color: #16a34a;
  font-size: 13px;
  font-weight: 600;
  padding: 5px 14px;
  border-radius: 20px;
}

.info-box {
  background: #eff6ff;
  border-radius: 10px;
  padding: 16px;
  font-size: 14px;
  color: #2563eb;
  line-height: 1.6;
}

.form-title {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 24px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 8px;
}

.required { 
  color: #dc2626; 
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  font-size: 15px;
  color: #111827;
  outline: none;
  transition: 0.2s;
  box-sizing: border-box;
  background: white;
  font-family: inherit;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #2563eb;
}

.form-bottom {
  margin-top: 6px; 
}

.btn-save {
  width: 100%;
  padding: 14px;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 16px;
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
  margin-bottom: 12px;
}

.error-msg {
  color: #dc2626;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 12px;
}

</style>