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
              ">
                {{ company.status }}
              </span>
            </td>
            <td>
              <div class="actions">

                <template v-if="company.status === 'Pending'">
                  <button class="btn-approve" @click="approveCompany(company)">Approve</button>
                  <button class="btn-reject"  @click="rejectCompany(company)">Reject</button>
                </template>

                <template v-if="company.status === 'Active'">
                  <button class="btn-view" @click="$router.push('/admin_dashboard/company_profile')">View Profile</button>
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

  </div>
</template>

<script>
export default {
  name: "AdminCompaniesView",

  data() {
    return {
      search: "",
      companies: [
        { id: 1, name: "Google",    industry: "Technology",  location: "Bangalore", package: "45 LPA", status: "Pending"  },
        { id: 2, name: "Microsoft", industry: "Technology",  location: "Hyderabad", package: "40 LPA", status: "Pending"  },
        { id: 3, name: "Amazon",    industry: "E-Commerce",  location: "Bangalore", package: "35 LPA", status: "Active"   },
        { id: 4, name: "Infosys",   industry: "IT Services", location: "Pune",      package: "8 LPA",  status: "Active"   },
        { id: 5, name: "TCS",       industry: "IT Services", location: "Mumbai",    package: "7 LPA",  status: "Rejected" },
        { id: 6, name: "Wipro",     industry: "IT Services", location: "Delhi",     package: "6 LPA",  status: "Pending"  },
        { id: 7, name: "Flipkart",  industry: "E-Commerce",  location: "Bangalore", package: "28 LPA", status: "Active"   },
        { id: 8, name: "Zomato",    industry: "Food Tech",   location: "Gurgaon",   package: "18 LPA", status: "Active"   },
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
    }
  },

  methods: {
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

</style>