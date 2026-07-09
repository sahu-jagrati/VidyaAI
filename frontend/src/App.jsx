import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';

import Landing        from './pages/Landing';
import Login          from './pages/Login';
import Home           from './pages/Home';
import SSCCgl         from './pages/SSCCgl';
import DailyChallenge from './pages/DailyChallenge';
import Leaderboard    from './pages/Leaderboard';
import Profile        from './pages/Profile';
import Contact        from './pages/Contact';
import About          from './pages/About';
import DailyNews      from './pages/DailyNews';
import PYQMains       from './pages/PYQMains';
import PYQAdvanced    from './pages/PYQAdvanced';
import TopicWise          from './pages/TopicWise';
import Pricing             from './pages/Pricing';
import SubscriptionSuccess from './pages/SubscriptionSuccess';
import SubscriptionFailed  from './pages/SubscriptionFailed';
import ManageSubscription  from './pages/ManageSubscription';

const Spinner = () => (
  <div className="min-h-screen flex items-center justify-center bg-gray-50">
    <div className="flex flex-col items-center gap-3">
      <div className="w-10 h-10 rounded-2xl bg-teal-700 flex items-center justify-center text-white font-bold text-xl shadow-lg animate-pulse">V</div>
      <p className="text-gray-400 text-sm">Loading…</p>
    </div>
  </div>
);

function ProtectedRoute({ children }) {
  const { isAuthenticated, loading } = useAuth();
  if (loading) return <Spinner />;
  return isAuthenticated ? children : <Navigate to="/login" replace />;
}

function AppRoutes() {
  const { isAuthenticated, loading } = useAuth();
  if (loading) return <Spinner />;

  return (
    <Routes>
      <Route path="/login" element={<Login />} />

      <Route path="/home"            element={<ProtectedRoute><Home /></ProtectedRoute>} />
      <Route path="/ssc-cgl"         element={<ProtectedRoute><SSCCgl /></ProtectedRoute>} />
      <Route path="/daily-challenge" element={<ProtectedRoute><DailyChallenge /></ProtectedRoute>} />
      <Route path="/leaderboard"     element={<ProtectedRoute><Leaderboard /></ProtectedRoute>} />
      <Route path="/profile"         element={<ProtectedRoute><Profile /></ProtectedRoute>} />
      <Route path="/contact"         element={<ProtectedRoute><Contact /></ProtectedRoute>} />
      <Route path="/about"           element={<ProtectedRoute><About /></ProtectedRoute>} />
      <Route path="/daily-news"      element={<ProtectedRoute><DailyNews /></ProtectedRoute>} />
      <Route path="/pyq/mains"       element={<ProtectedRoute><PYQMains /></ProtectedRoute>} />
      <Route path="/pyq/advanced"    element={<ProtectedRoute><PYQAdvanced /></ProtectedRoute>} />
      <Route path="/topic-wise"      element={<ProtectedRoute><TopicWise /></ProtectedRoute>} />

      <Route path="/pricing"                  element={<Pricing />} />
      <Route path="/subscription/success"     element={<ProtectedRoute><SubscriptionSuccess /></ProtectedRoute>} />
      <Route path="/subscription/failed"      element={<ProtectedRoute><SubscriptionFailed /></ProtectedRoute>} />
      <Route path="/subscription/manage"      element={<ProtectedRoute><ManageSubscription /></ProtectedRoute>} />

      <Route path="/"  element={<Landing />} />
      <Route path="*"  element={<Navigate to="/" replace />} />
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
