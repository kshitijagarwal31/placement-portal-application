<template>
  <div>

    <button class="btn-back" @click="$router.back()">← Back</button>

    <div class="profile-box">

      <div class="profile-header">
        <div class="avatar">{{ company.name.charAt(0) }}</div>
        <div>
          <h1>{{ company.name }}</h1>
          <p>{{ company.email }} · {{ company.username }}</p>
        </div>
        <span :class="company.is_active ? 'badge-active' : 'badge-inactive'">
          {{ company.is_active ? 'Active' : 'Inactive' }}
        </span>
      </div>

      <div class="info-grid">
        <div class="info-item">
          <p class="info-label">Industry</p>
          <p class="info-value">{{ company.industry }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Address</p>
          <p class="info-value">{{ company.address }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">HR Contact</p>
          <p class="info-value">{{ company.hr_contact_number }}</p>
        </div>
        <div class="info-item">
          <p class="info-label">Website</p>
          <p class="info-value">
            <a :href="company.website_link" target="_blank" class="website-link">{{ company.website_link || '—' }}</a>
          </p>
        </div>
        <div class="info-item">
          <p class="info-label">Description</p>
          <p class="info-value">{{ company.description || '—' }}</p>
        </div>
      </div>

    </div>

    <div class="section-title">
      <h2>Placement Drives</h2>
      <p>All drives posted by this company</p>
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Drive Name</th>
            <th>Start Date</th>
            <th>Last Date</th>
            <th>Package</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(drive, index) in company.drives" :key="drive.id">
            <td>{{ index + 1 }}</td>
            <td>{{ drive.job_title }}</td>
            <td>{{ drive.start_date }}</td>
            <td>{{ drive.last_date }}</td>
            <td>{{ drive.salary }}</td>
            <td>
              <span :class="
                drive.status === 'Pending'   ? 'badge-pending'   :
                drive.status === 'Upcoming'  ? 'badge-upcoming'  :
                drive.status === 'Ongoing'   ? 'badge-ongoing'   :
                drive.status === 'Completed' ? 'badge-completed' :
                'badge-rejected'
              ">{{ drive.status }}</span>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="company.drives.length === 0" class="empty">
        No drives found
      </div>

    </div>

  </div>
</template>

<script>
export default {
  name: "AdminCompanyProfileView",

  data() {
    return {
      company: {
        id: 1,
        name: "Google",
        username: "google_hr",
        email: "hr@google.com",
        is_active: true,
        industry: "Technology",
        address: "Bangalore, India",
        hr_contact_number: "+91 9876543210",
        website_link: "https://google.com",
        description: "Leading technology company.",
        drives: [
          { id: 1, job_title: "Software Engineer",  start_date: "25 May 2026", last_date: "30 May 2026", salary: "45 LPA", status: "Upcoming"  },
          { id: 2, job_title: "Frontend Developer", start_date: "20 May 2026", last_date: "28 May 2026", salary: "35 LPA", status: "Ongoing"   },
          { id: 3, job_title: "Backend Developer",  start_date: "10 May 2026", last_date: "18 May 2026", salary: "40 LPA", status: "Completed" },
        ]
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

.btn-back:hover {
  text-decoration: underline;
}

.profile-box {
  background: white;
  border-radius: 18px;
  padding: 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  margin-bottom: 28px;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding-bottom: 20px;
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

.profile-header span {
  margin-left: auto;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 14px;
}

.info-item {
  background: #f9fafb;
  padding: 14px;
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

.website-link {
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
}

.website-link:hover {
  text-decoration: underline;
}

.section-title {
  margin-bottom: 16px;
}

.section-title h2 {
  font-size: 18px;
  color: #111827;
  font-weight: 600;
  margin-bottom: 4px;
}

.section-title p {
  font-size: 13px;
  color: #6b7280;
}

.table-box {
  background: white;
  border-radius: 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  background: #f9fafb;
}

th {
  padding: 16px 20px;
  text-align: left;
  font-size: 14px;
  color: #6b7280;
  font-weight: 600;
  border-bottom: 1px solid #e5e7eb;
}

td {
  padding: 16px 20px;
  font-size: 14px;
  color: #111827;
  border-bottom: 1px solid #f3f4f6;
}

tr:last-child td {
  border-bottom: none;
}

tr:hover td {
  background: #f9fafb;
}

.empty {
  text-align: center;
  color: #9ca3af;
  font-size: 15px;
  padding: 40px 0;
}

.badge-active {
  background: #dcfce7;
  color: #16a34a;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-inactive {
  background: #fee2e2;
  color: #dc2626;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-pending {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-upcoming {
  background: #dbeafe;
  color: #2563eb;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-ongoing {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-completed {
  background: #f3f4f6;
  color: #6b7280;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-rejected {
  background: #fee2e2;
  color: #dc2626;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

</style>