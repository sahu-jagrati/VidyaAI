import { useState } from 'react';
import Layout from '../components/Layout';

const socials = [
  { icon: '💼', label: 'LinkedIn',  href: '#', bg: 'bg-blue-50',   border: 'border-blue-200',   text: 'text-blue-700'   },
  { icon: '📷', label: 'Instagram', href: '#', bg: 'bg-pink-50',   border: 'border-pink-200',   text: 'text-pink-700'   },
  { icon: '🐙', label: 'GitHub',    href: '#', bg: 'bg-gray-50',   border: 'border-gray-200',   text: 'text-gray-700'   },
];

export default function Contact() {
  const [form, setForm] = useState({ name: '', email: '', message: '' });
  const [sent, setSent] = useState(false);

  const handleChange = e => setForm(prev => ({ ...prev, [e.target.name]: e.target.value }));

  const handleSubmit = e => {
    e.preventDefault();
    if (!form.name || !form.email || !form.message) return;
    setSent(true);
  };

  return (
    <Layout>
      <div className="max-w-2xl mx-auto fade-in">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900">Contact Us ✉️</h1>
          <p className="text-gray-400 text-sm mt-1">Have a question or feedback? We'd love to hear from you.</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-5 gap-5">

          {/* Form */}
          <div className="sm:col-span-3 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
            {sent ? (
              <div className="flex flex-col items-center justify-center py-8 text-center">
                <span className="text-5xl mb-4">🎉</span>
                <h3 className="text-gray-900 font-bold text-lg mb-2">Message Sent!</h3>
                <p className="text-gray-400 text-sm">Thanks for reaching out. We'll get back to you within 24 hours.</p>
                <button
                  onClick={() => { setForm({ name: '', email: '', message: '' }); setSent(false); }}
                  className="mt-6 px-6 py-2.5 bg-teal-700 hover:bg-teal-800 text-white text-sm font-semibold rounded-xl transition-colors shadow-sm shadow-teal-200"
                >
                  Send another
                </button>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <label className="block text-gray-700 text-sm font-semibold mb-1.5">Name</label>
                  <input
                    name="name" value={form.name} onChange={handleChange}
                    placeholder="Rahul Sharma"
                    className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 text-sm focus:outline-none focus:border-teal-500 focus:ring-2 focus:ring-teal-100 transition-all"
                  />
                </div>
                <div>
                  <label className="block text-gray-700 text-sm font-semibold mb-1.5">Email</label>
                  <input
                    name="email" type="email" value={form.email} onChange={handleChange}
                    placeholder="you@example.com"
                    className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 text-sm focus:outline-none focus:border-teal-500 focus:ring-2 focus:ring-teal-100 transition-all"
                  />
                </div>
                <div>
                  <label className="block text-gray-700 text-sm font-semibold mb-1.5">Message</label>
                  <textarea
                    name="message" value={form.message} onChange={handleChange}
                    rows={5} placeholder="Your message here..."
                    className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 text-sm focus:outline-none focus:border-teal-500 focus:ring-2 focus:ring-teal-100 transition-all resize-none"
                  />
                </div>
                <button
                  type="submit"
                  className="w-full bg-teal-700 hover:bg-teal-800 text-white font-semibold py-3 rounded-xl transition-colors text-sm shadow-md shadow-teal-200"
                >
                  Send Message →
                </button>
              </form>
            )}
          </div>

          {/* Right panel */}
          <div className="sm:col-span-2 space-y-4">
            <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
              <h3 className="text-gray-900 font-semibold mb-4">Get in touch</h3>
              <div className="space-y-3">
                <div className="flex items-center gap-3 text-sm">
                  <span className="w-9 h-9 rounded-xl bg-teal-50 border border-teal-200 flex items-center justify-center text-lg shrink-0">📧</span>
                  <span className="text-gray-600">support@vidyaai.in</span>
                </div>
                <div className="flex items-center gap-3 text-sm">
                  <span className="w-9 h-9 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-lg shrink-0">⏰</span>
                  <span className="text-gray-600">Response within 24 hours</span>
                </div>
                <div className="flex items-center gap-3 text-sm">
                  <span className="w-9 h-9 rounded-xl bg-orange-50 border border-orange-200 flex items-center justify-center text-lg shrink-0">🇮🇳</span>
                  <span className="text-gray-600">India · Hindi &amp; English</span>
                </div>
              </div>
            </div>

            <div className="bg-white border border-gray-200 rounded-2xl p-5 shadow-sm">
              <h3 className="text-gray-900 font-semibold mb-4">Follow us</h3>
              <div className="space-y-2">
                {socials.map(s => (
                  <a key={s.label} href={s.href}
                    className={`flex items-center gap-3 px-4 py-2.5 rounded-xl border ${s.bg} ${s.border} ${s.text} text-sm font-medium hover:opacity-80 transition-opacity`}>
                    <span className="text-xl">{s.icon}</span>
                    {s.label}
                  </a>
                ))}
              </div>
            </div>

            <div className="bg-teal-50 border border-teal-200 rounded-2xl p-5">
              <p className="text-teal-700 text-xs font-bold uppercase tracking-wider mb-1">📚 Free Forever</p>
              <p className="text-teal-600 text-sm">VidyaAi is completely free. No subscription, no hidden charges.</p>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}
