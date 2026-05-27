<template>
  <div class="page">

    <Navbar />

    <div class="register-page">

      <div class="register-card">

        <div class="top-section">
          <h2>Create Account</h2>
          <p>Register to continue to PlaceMe Portal</p>
        </div>

        <div v-if="errorMessage" class="error-box">
          {{ errorMessage }}
        </div>

        <form @submit.prevent="handleRegister">

          <div class="input-group">
            <label>Full Name</label>
            <input type="text" v-model="fullName" placeholder="Enter your name" required />
          </div>

          <div class="input-group">
            <label>Username</label>
            <input type="text" v-model="username" placeholder="Enter username" required />
          </div>

          <div class="input-group">
            <label>Email</label>
            <input type="email" v-model="email" placeholder="Enter email" required />
          </div>

          <div class="input-group">
            <label>Role</label>
            <select v-model="role" required>
              <option disabled value="">Select role</option>
              <option value="student">Student</option>
              <option value="company">Company</option>
            </select>
          </div>

          <div class="input-group">
            <label>Password</label>

            <div class="password-box">
              <input
                :type="showPassword ? 'text' : 'password'"
                v-model="password"
                placeholder="Create password"
                required
              />

              <button type="button" class="show-btn" @click="showPassword = !showPassword">
                {{ showPassword ? 'Hide' : 'Show' }}
              </button>
            </div>
          </div>

          <label class="terms">
            <input type="checkbox" required />
            <span>I agree to terms & conditions</span>
          </label>

          <button type="submit" class="btn" :disabled="loading">
            <span v-if="loading">Creating Account...</span>
            <span v-else>Register</span>
          </button>

        </form>

        <p class="bottom-text">
          Already have an account?
          <router-link to="/login">Login</router-link>
        </p>

      </div>

    </div>

    <Footer />

  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue"
import Footer from "../components/Footer.vue"
import axios from "axios"

export default {
  name: "RegisterView",
  components: {
    Navbar,
    Footer
  },

  data() {
    return {
      fullName: "",
      username: "",
      email: "",
      role: "",
      password: "",
      showPassword: false,
      loading: false,
      errorMessage: ""
    }
  },

  methods: {
    async handleRegister() {
      this.errorMessage = ""
      this.loading = true

      const url = this.role === "student"
        ? "http://localhost:5000/register/student"
        : "http://localhost:5000/register/company"

      try {
        const res = await axios.post(url, {
          name:     this.fullName,
          username: this.username,
          email:    this.email,
          password: this.password
        })
        alert(res.data.message)
        this.$router.push("/login")
      
      } catch (err) {
        this.errorMessage = err.response.data.message 
      } finally {
        this.loading = false
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

.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: Arial, sans-serif;
}

.register-page {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 60px 20px;
  background: #f5f7fb;
}

.register-card {
  width: 100%;
  max-width: 500px;
  background: #fff;
  padding: 48px;  
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.06);
}

.top-section {
  text-align: center;
  margin-bottom: 25px;
}

.top-section h2 {
  font-size: 36px; 
  margin-bottom: 8px;
}

.top-section p {
  color: #6b7280;
  font-size: 14px;
}

.error-box {
  background: #fef2f2;
  color: #dc2626;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 15px;
  font-size: 14px;
}

.input-group {
  margin-bottom: 18px;
}

.input-group label {
  display: block;
  margin-bottom: 6px;
  font-size: 14px;
  font-weight: 600;
}

.input-group input,
.input-group select {
  width: 100%;
  padding: 14px;  
  border: 1px solid #d1d5db;
  border-radius: 8px;
  outline: none;
  font-size: 15px;  
}

.input-group input:focus,
.input-group select:focus {
  border-color: #2563eb;
}

.password-box {
  position: relative;
}

.show-btn {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  border: none;
  background: none;
  color: #2563eb;
  cursor: pointer;
}

.terms {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 20px;
  font-size: 13px;
  color: #6b7280;
}

.btn {
  width: 100%;
  padding: 14px;    
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  font-size: 15px;
  cursor: pointer;
}

.btn:hover {
  background: #1d4ed8;
}

.bottom-text {
  text-align: center;
  margin-top: 18px;
  font-size: 14px;
  color: #6b7280;
}

.bottom-text a {
  color: #2563eb;
  font-weight: bold;
  text-decoration: none;
}

</style>