import { useState } from 'react';
import Navbar from './Navbar';
import Sidebar from './Sidebar';

export default function Layout({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="min-h-screen bg-[#0b0015]">
      <Navbar onMenuToggle={() => setSidebarOpen(prev => !prev)} />
      <Sidebar isOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} />

      {/* Main content — offset for fixed navbar + sidebar */}
      <main className="pt-16 lg:pl-60 min-h-screen">
        <div className="p-4 sm:p-6 lg:p-8 max-w-6xl mx-auto fade-in">
          {children}
        </div>
      </main>
    </div>
  );
}
