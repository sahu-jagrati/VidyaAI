import { useState, useEffect } from 'react';
import Navbar from './Navbar';
import Sidebar from './Sidebar';

export default function Layout({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  useEffect(() => {
    setSidebarOpen(window.innerWidth >= 1024);
  }, []);

  return (
    <div className="min-h-screen" style={{ backgroundColor: '#F5F7F8' }}>
      <Navbar
        onMenuToggle={() => setSidebarOpen(prev => !prev)}
        sidebarOpen={sidebarOpen}
      />
      <Sidebar isOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} />
      <main className={`pt-16 min-h-screen transition-all duration-250 ease-in-out ${sidebarOpen ? 'lg:pl-60' : ''}`}>
        <div className="p-4 sm:p-6 lg:p-8 max-w-6xl mx-auto fade-in">
          {children}
        </div>
      </main>
    </div>
  );
}
