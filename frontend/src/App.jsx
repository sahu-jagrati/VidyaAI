import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';

import Login          from './pages/Login';
import Home           from './pages/Home';
import SSCCgl         from './pages/SSCCgl';
import DailyChallenge from './pages/DailyChallenge';
import Leaderboard    from './pages/Leaderboard';
import Profile        from './pages/Profile';
import Contact        from './pages/Contact';
import About          from './pages/About';

function ProtectedRoute({ children }) {
  const { isAuthenticated, loading } = useAuth();
  if (loading) return null;
  return isAuthenticated ? children : <Navigate to="/login" replace />;
}

function AppRoutes() {
  const { isAuthenticated, loading } = useAuth();
  if (loading) return null;

  return (
    <Routes>
      <Route path="/login" element={isAuthenticated ? <Navigate to="/home" replace /> : <Login />} />

      <Route path="/home"            element={<ProtectedRoute><Home /></ProtectedRoute>} />
      <Route path="/ssc-cgl"         element={<ProtectedRoute><SSCCgl /></ProtectedRoute>} />
      <Route path="/daily-challenge" element={<ProtectedRoute><DailyChallenge /></ProtectedRoute>} />
      <Route path="/leaderboard"     element={<ProtectedRoute><Leaderboard /></ProtectedRoute>} />
      <Route path="/profile"         element={<ProtectedRoute><Profile /></ProtectedRoute>} />
      <Route path="/contact"         element={<ProtectedRoute><Contact /></ProtectedRoute>} />
      <Route path="/about"           element={<ProtectedRoute><About /></ProtectedRoute>} />

      <Route path="/"  element={<Navigate to={isAuthenticated ? '/home' : '/login'} replace />} />
      <Route path="*"  element={<Navigate to={isAuthenticated ? '/home' : '/login'} replace />} />
    </Routes>
  );
}

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <AppRoutes />
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
