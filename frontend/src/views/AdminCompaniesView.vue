<template>
  <div>

    <div class="topbar">
      <div>
        <h1>Companies</h1>
        <p>Manage all registered companies</p>
      </div>
      <input
        v-model="search"
        class="search-input"
        type="text"
        placeholder="Search by name, industry or location..."
      />
    </div>

    <div class="table-box">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Company</th>
            <th>Industry</th>
            <th>Location</th>
            <th>Package</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(company, index) in filteredCompanies" :key="company.id">
            <td>{{ index + 1 }}</td>
            <td>{{ company.name }}</td>
            <td>{{ company.industry }}</td>
            <td>{{ company.location }}</td>
            <td>{{ company.package }}</td>
            <td>
              <span :class="
                company.status === 'Pending'  ? 'badge-pending'  :
                company.status === 'Active'   ? 'badge-active'   :
                'badge-rejected'
              ">{{ company.status }}</span>
            </td>
            <td>
              <div class="actions">

                <template v-if="company.status === 'Pending'">
                  <button class="btn-approve" @click="approveCompany(company)">Approve</button>
                  <button class="btn-reject"  @click="rejectCompany(company)">Reject</button>
                </template>

                <template v-if="company.status === 'Active'">
                  <button class="btn-view" @click="viewProfile(company)">View Profile</button>
                </template>

                <template v-if="company.status === 'Rejected'">
                  <span class="text-rejected">—</span>
                </template>

              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="filteredCompanies.length === 0" class="empty">
        No companies found
      </div>
    </div>

    <div v-if="selectedCompany" class="modal-overlay" @click.self="selectedCompany = null">
      <div class="modal">

        <div class="modal-header">
          <h3>Company Profile</h3>
          <button class="btn-close" @click="selectedCompany = null">✕</button>
        </div>

        <div class="detail-top">
          <div class="avatar-lg">{{ selectedCompany.name.charAt(0) }}</div>
          <div>
            <h4>{{ selectedCompany.name }}</h4>
            <p>{{ selectedCompany.industry }} · {{ selectedCompany.location }}</p>
          </div>
          <span :class="
            selectedCompany.status === 'Active'  ? 'badge-active'  :
            selectedCompany.status === 'Pending' ? 'badge-pending' :
            'badge-rejected'
          ">{{ selectedCompany.status }}</span>
        </div>

        <div class="detail-rows">
          <div class="detail-row">
            <span class="detail-label">Full Name</span>
            <span class="detail-value">{{ selectedCompany.full_name }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Username</span>
            <span class="detail-value">{{ selectedCompany.username }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Email</span>
            <span class="detail-value">{{ selectedCompany.email }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Industry</span>
            <span class="detail-value">{{ selectedCompany.industry }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">HR Contact</span>
            <span class="detail-value">{{ selectedCompany.hr_contact }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Address</span>
            <span class="detail-value">{{ selectedCompany.address }}</span>
          </div>
          <div class="detail-row">
            <span class="detail-label">Website</span>
            <a :href="selectedCompany.website" target="_blank" class="website-link">🌐 {{ selectedCompany.website }}</a>
          </div>
          <div class="detail-row">
            <span class="detail-label">Description</span>
            <span class="detail-value">{{ selectedCompany.description }}</span>
          </div>
        </div>

        <div class="app-section">
          <h4 class="app-section-title">
            Placement Drives
            <span class="app-count">{{ companyDrives.length }}</span>
          </h4>

          <div v-if="companyDrives.length === 0" class="app-empty">
            No drives posted yet
          </div>

          <div class="app-table-box" v-else>
            <table class="app-table">
              <thead>
                <tr>
                  <th>S.No</th>
                  <th>Role</th>
                  <th>Package</th>
                  <th>Last Date</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(drive, index) in companyDrives" :key="drive.id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ drive.role }}</td>
                  <td>{{ drive.package }}</td>
                  <td>{{ drive.last_date }}</td>
                  <td>
                    <span :class="
                      drive.status === 'Upcoming'  ? 'status-upcoming'  :
                      drive.status === 'Ongoing'   ? 'status-ongoing'   :
                      'status-completed'
                    ">{{ drive.status }}</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "AdminCompaniesView",

  data() {
    return {
      search: "",
      selectedCompany: null,
      companies: [
        { id: 1, name: "Google",    full_name: "Google India Pvt Ltd",    username: "google_hr",    email: "hr@google.com",    industry: "Technology",  hr_contact: "+91 9800000001", location: "Bangalore", address: "Bangalore, Karnataka", website: "www.google.com",    package: "45 LPA", description: "Leading tech company.",      status: "Pending"  },
        { id: 2, name: "Microsoft", full_name: "Microsoft India Pvt Ltd", username: "microsoft_hr", email: "hr@microsoft.com", industry: "Technology",  hr_contact: "+91 9800000002", location: "Hyderabad", address: "Hyderabad, Telangana",  website: "www.microsoft.com", package: "40 LPA", description: "Global software company.",    status: "Pending"  },
        { id: 3, name: "Amazon",    full_name: "Amazon India Pvt Ltd",    username: "amazon_hr",    email: "hr@amazon.com",    industry: "E-Commerce",  hr_contact: "+91 9800000003", location: "Bangalore", address: "Bangalore, Karnataka", website: "www.amazon.com",    package: "35 LPA", description: "World's largest e-commerce.", status: "Active"   },
        { id: 4, name: "Infosys",   full_name: "Infosys Limited",         username: "infosys_hr",   email: "hr@infosys.com",   industry: "IT Services", hr_contact: "+91 9800000004", location: "Pune",      address: "Pune, Maharashtra",    website: "www.infosys.com",   package: "8 LPA",  description: "Top IT services company.",   status: "Active"   },
        { id: 5, name: "TCS",       full_name: "Tata Consultancy Services",username: "tcs_hr",      email: "hr@tcs.com",       industry: "IT Services", hr_contact: "+91 9800000005", location: "Mumbai",    address: "Mumbai, Maharashtra",  website: "www.tcs.com",       package: "7 LPA",  description: "Largest IT company India.",  status: "Rejected" },
        { id: 6, name: "Wipro",     full_name: "Wipro Technologies",      username: "wipro_hr",     email: "hr@wipro.com",     industry: "IT Services", hr_contact: "+91 9800000006", location: "Delhi",     address: "Delhi, India",         website: "www.wipro.com",     package: "6 LPA",  description: "Global IT solutions.",       status: "Pending"  },
        { id: 7, name: "Flipkart",  full_name: "Flipkart India Pvt Ltd",  username: "flipkart_hr",  email: "hr@flipkart.com",  industry: "E-Commerce",  hr_contact: "+91 9800000007", location: "Bangalore", address: "Bangalore, Karnataka", website: "www.flipkart.com",  package: "28 LPA", description: "India's top e-commerce.",    status: "Active"   },
        { id: 8, name: "Zomato",    full_name: "Zomato India Pvt Ltd",    username: "zomato_hr",    email: "hr@zomato.com",    industry: "Food Tech",   hr_contact: "+91 9800000008", location: "Gurgaon",   address: "Gurgaon, Haryana",     website: "www.zomato.com",    package: "18 LPA", description: "Leading food delivery app.",  status: "Active"   },
      ],
      drives: [
        { id: 1, company_id: 3, role: "Backend Developer",    package: "35 LPA", last_date: "20 May 2026", status: "Ongoing"   },
        { id: 2, company_id: 3, role: "Data Engineer",        package: "30 LPA", last_date: "25 May 2026", status: "Upcoming"  },
        { id: 3, company_id: 4, role: "Systems Engineer",     package: "8 LPA",  last_date: "15 May 2026", status: "Completed" },
        { id: 4, company_id: 7, role: "Frontend Developer",   package: "28 LPA", last_date: "30 May 2026", status: "Upcoming"  },
        { id: 5, company_id: 7, role: "Full Stack Developer", package: "25 LPA", last_date: "18 May 2026", status: "Ongoing"   },
        { id: 6, company_id: 8, role: "Full Stack Developer", package: "18 LPA", last_date: "18 May 2026", status: "Ongoing"   },
      ]
    }
  },

  computed: {
    filteredCompanies() {
      const q = this.search.toLowerCase()
      return this.companies.filter(c =>
        c.name.toLowerCase().includes(q)     ||
        c.industry.toLowerCase().includes(q) ||
        c.location.toLowerCase().includes(q)
      )
    },
    companyDrives() {
      if (!this.selectedCompany) return []
      return this.drives.filter(d => d.company_id === this.selectedCompany.id)
    }
  },

  methods: {
    viewProfile(company) {
      this.selectedCompany = company
    },
    approveCompany(company) { company.status = 'Active'   },
    rejectCompany(company)  { company.status = 'Rejected' },
  }
}
</script>

<style scoped>

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.topbar h1 {
  font-size: 34px;
  color: #111827;
  margin-bottom: 4px;
}

.topbar p {
  color: #6b7280;
  font-size: 15px;
}

.search-input {
  padding: 11px 14px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  font-size: 14px;
  color: #111827;
  width: 280px;
  outline: none;
  transition: 0.2s;
  background: white;
}

.search-input:focus {
  border-color: #2563eb;
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
  font-size: 15px;
  color: #111827;
  border-bottom: 1px solid #f3f4f6;
  font-weight: 600;
}

tr:last-child td {
  border-bottom: none;
}

tr:hover td {
  background: #f9fafb;
}

.actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

.btn-approve {
  background: #dcfce7;
  color: #16a34a;
  border: none;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-approve:hover {
  background: #bbf7d0;
}

.btn-reject {
  background: #fee2e2;
  color: #dc2626;
  border: none;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-reject:hover {
  background: #fecaca;
}

.btn-view {
  background: #eff6ff;
  color: #2563eb;
  border: none;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-view:hover {
  background: #dbeafe;
}

.text-rejected {
  color: #9ca3af;
  font-size: 15px;
}

.badge-pending {
  background: #fef9c3;
  color: #ca8a04;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-active {
  background: #dcfce7;
  color: #16a34a;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.badge-rejected {
  background: #fee2e2;
  color: #dc2626;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.empty {
  text-align: center;
  color: #9ca3af;
  font-size: 15px;
  padding: 40px 0;
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: white;
  border-radius: 18px;
  width: 620px;
  max-width: 90%;
  max-height: 85vh;
  overflow-y: auto;
  padding: 28px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  position: sticky;
  top: 0;
  background: white;
  z-index: 1;
  padding-bottom: 16px;
  border-bottom: 1px solid #f3f4f6;
}

.modal-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}

.btn-close {
  background: #f3f4f6;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  font-size: 14px;
  cursor: pointer;
  color: #374151;
}

.detail-top {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid #f3f4f6;
}

.avatar-lg {
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

.detail-top h4 {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 4px;
  flex: 1;
}

.detail-top p {
  font-size: 13px;
  color: #6b7280;
}

.detail-rows {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 28px;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
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

.website-link {
  color: #2563eb;
  font-weight: 600;
  font-size: 14px;
  text-decoration: none;
}

.website-link:hover {
  text-decoration: underline;
}

.app-section {
  margin-top: 4px;
}

.app-section-title {
  font-size: 15px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.app-count {
  background: #eff6ff;
  color: #2563eb;
  padding: 2px 10px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.app-empty {
  text-align: center;
  color: #9ca3af;
  font-size: 14px;
  padding: 20px 0;
}

.app-table-box {
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  overflow: hidden;
}

.app-table {
  width: 100%;
  border-collapse: collapse;
}

.app-table thead {
  background: #f9fafb;
}

.app-table th {
  padding: 12px 16px;
  text-align: left;
  font-size: 13px;
  color: #6b7280;
  font-weight: 600;
  border-bottom: 1px solid #e5e7eb;
}

.app-table td {
  padding: 12px 16px;
  font-size: 14px;
  color: #111827;
  border-bottom: 1px solid #f3f4f6;
  font-weight: 500;
}

.app-table tr:last-child td {
  border-bottom: none;
}

.app-table tr:hover td {
  background: #f9fafb;
}

.status-upcoming {
  background: #dbeafe;
  color: #2563eb;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.status-ongoing {
  background: #fef9c3;
  color: #ca8a04;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.status-completed {
  background: #dcfce7;
  color: #16a34a;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}


</style>