import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import PrivateRoute from './components/PrivateRoute';  // Assume this is a custom component that handles protected routes
import Login from './pages/Login';
import Register from './pages/Register';
import UserProfile from './pages/UserProfile';
import PasswordReset from './pages/PasswordReset';


function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/reset-password" component={PasswordReset} />
        <PrivateRoute exact path="/user" component={UserProfile} />
        {/* Other protected routes */}
      </Switch>
    </Router>
  );
}

export default App;
