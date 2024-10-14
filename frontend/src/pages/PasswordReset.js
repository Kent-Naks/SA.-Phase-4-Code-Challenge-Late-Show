import React, { useState } from 'react';
import axios from '../api';

function PasswordReset() {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // You'd typically implement an endpoint to handle sending password reset emails.
      await axios.post('/reset-password', { email });
      setMessage('Password reset link sent to your email');
    } catch (err) {
      setMessage('Error sending reset email');
    }
  };

  