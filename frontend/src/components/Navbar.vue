<template>

  <nav class="navbar">

    <div class="navbar-left">

      <router-link to="/" class="logo-area">

        <div class="logo">
          🎓
        </div>

        <div>

          <h2 class="logo-title">
            PlaceMe
          </h2>

          <p class="logo-subtitle">
            Placement Portal
          </p>

        </div>

      </router-link>

    </div>

    <div class="navbar-right">

      <router-link to="/" class="nav-link">
        Home
      </router-link>

      <router-link to="/login" class="nav-link">
        Login
      </router-link>

      <router-link to="/register" class="register-btn">
        Register
      </router-link>

    </div>

  </nav>

</template>

<script>

export default {

  name: "Navbar"

}

</script>

<style scoped>

*{
  margin:0;
  padding:0;
  box-sizing:border-box;
}

.navbar{
  width:100%;
  height:80px;
  padding:0 60px;
  display:flex;
  justify-content:space-between;
  align-items:center;
  background:#2563eb;
  position:sticky;
  top:0;
  z-index:1000;
  box-shadow:0 4px 16px rgba(0,0,0,0.08);
}

.logo-area{
  display:flex;
  align-items:center;
  gap:12px;
  text-decoration:none;
}

.logo{
  width:50px;
  height:50px;
  background:white;
  border-radius:14px;
  display:flex;
  justify-content:center;
  align-items:center;
  font-size:26px;
}

.logo-title{
  font-size:24px;
  font-weight:700;
  color:white;
}

.logo-subtitle{
  font-size:12px;
  color:#dbeafe;
  margin-top:2px;
}

.navbar-right{
  display:flex;
  align-items:center;
  gap:14px;
}

.nav-link{
  text-decoration:none;
  color:white;
  font-size:15px;
  font-weight:600;
  padding:10px 14px;
  border-radius:8px;
  transition:0.2s;
}

.nav-link:hover{
  background:rgba(255,255,255,0.15);
}

.register-btn{
  text-decoration:none;
  background:white;
  color:#2563eb;
  padding:12px 22px;
  border-radius:10px;
  font-weight:700;
  transition:0.2s;
}

.register-btn:hover{
  background:#e0e7ff;
}

@media(max-width:768px){

  .navbar{
    padding:18px 20px;
    height:auto;
    flex-direction:column;
    gap:18px;
  }

  .navbar-right{
    width:100%;
    justify-content:center;
    flex-wrap:wrap;
  }

  .logo-title{
    font-size:22px;
  }

}

</style>