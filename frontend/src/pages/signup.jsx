import React, { useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'

const Signup = () => {
  const [credentials, setCredentials] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
    role: ''
  })
  console.log(location.state?.role)

  const navigate = useNavigate()
  const location = useLocation()
  const role = location.state?.role || 'patient'
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (credentials.password !== credentials.confirmPassword) {
      alert('Passwords do not match');
      return;
    }
    console.log('Signup attempt for role:', role, 'with credentials:', credentials)
    try {
      const response = await fetch('http://localhost:8000/api/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials)
      });
  
      const data = await response.json();
  
      if (response.ok) {
        console.log('Signup successful:', data);
        // Show success message to user
        alert('Signup successful! Please login.');
        navigate('/login', { state: { role } });
      } else {
        // Handle error response from server
        console.error('Signup failed:', data.message);
        alert(data.message || 'Signup failed. Please try again.');
      }
    } catch (error) {
      console.error('Error during signup:', error);
      alert('An error occurred during signup. Please try again.');
    }
  }

  return (
    <div className="signup-container">
      <h2>Signup as {role}</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            type="text"
            placeholder="Username"
            value={credentials.username}
            onChange={(e) => setCredentials({...credentials, username: e.target.value})}
          />
        </div>
        <div className="form-group">
          <input
            type="text"
            placeholder="Email"
            value={credentials.email}
            onChange={(e) => setCredentials({...credentials, email: e.target.value})}
          />
        </div>
        <div className="form-group">
          <input
            type="password"
            placeholder="Password"
            value={credentials.password}
            onChange={(e) => setCredentials({...credentials, password: e.target.value})}
          />
        </div>
        <div className="form-group">
          <input
            type="password"
            placeholder="ConfirmPassword"
            value={credentials.confirmPassword}
            onChange={(e) => setCredentials({...credentials, confirmPassword: e.target.value})}
          />
        </div>
        <div className="form-group">
          <select value={credentials.role} onChange={(e) => setCredentials({...credentials, role: e.target.value})}>
            <option value="patient">Patient</option>
            <option value="doctor">Doctor</option>
            <option value="admin">Admin</option>
          </select>
        </div>
        <button type="submit">Signup</button>
      </form>
      <div className="button-container">
        <button onClick={() => navigate('/')}>Back to Home</button>
        <p>Already have an account ?</p>
        <button onClick={() => navigate('/login')}>Login</button>
      </div>
    </div>
  )
}

export default Signup