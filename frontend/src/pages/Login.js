import React, { useState } from 'react';
import axios from '../api';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/login', { username, password });
      localStorage.setItem('token', response.data.access_token);
      // Redirect to user profile or protected route
    } catch (err) {
      setError('Invalid credentials');
    }
  };
