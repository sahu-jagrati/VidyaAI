import { useState } from 'react';
import Layout from '../components/Layout';

const socials = [
  { icon: '💼', label: 'LinkedIn',  href: '#', color: 'text-blue-400',   bg: 'bg-blue-500/10',   border: 'border-blue-500/30'   },
  { icon: '📷', label: 'Instagram', href: '#', color: 'text-pink-400',   bg: 'bg-pink-500/10',   border: 'border-pink-500/30'   },
  { icon: '🐙', label: 'GitHub',    href: '#', color: 'text-gray-300',   bg: 'bg-white/5',       border: 'border-white/10'      },
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
        <div className="mb-8">
          <h1 className="text-2xl font-bold text-white">Contact Us ✉️</h1>
          <p className="text-gray-400 text-sm mt-1">Have a question or feedback? We'd love to hear from you.</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-5 gap-6">
          {/* Form */}
          <div className="sm:col-span-3 bg-[#130022] border border-purple-800/30 rounded-2xl p-6">
            {sent ? (
              <div className="flex flex-col items-center justify-center py-8 text-center">
                <span className="text-5xl mb-4">🎉</span>
                <h3 className="text-white font-bold text-lg mb-2">Message Sent!</h3>
                <p className="text-gray-400 text-sm">Thanks for reaching out. We'll get back to you within 24 hours.</p>
                <button
                  onClick={() => { setForm({ name: '', email: '', message: '' }); setSent(false); }}
                  className="mt-6 px-6 py-2.5 bg-linear-to-r from-rose-600 to-violet-600 hover:from-rose-500 hover:to-violet-500 text-white text-sm font-medium rounded-xl transition-all duration-200"
                >
                  Send another
                </button>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <label className="block text-gray-400 text-xs font-medium mb-1.5 uppercase tracking-wider">Name</label>
                  <input
                    name="name" value={form.name} onChange={handleChange}
                    placeholder="Rahul Sharma"
                    className="w-full bg-white/5 border border-purple-800/40 rounded-xl px-4 py-3 text-white placeholder-gray-600 text-sm focus:outline-none focus:border-rose-500/60 transition-colors"
                  />
                </div>
                <div>
                  <label className="block text-gray-400 text-xs font-medium mb-1.5 uppercase tracking-wider">Email</label>
                  <input
                    name="email" type="email" value={form.email} onChange={handleChange}
                    placeholder="you@example.com"
                    className="w-full bg-white/5 border border-purple-800/40 rounded-xl px-4 py-3 text-white placeholder-gray-600 text-sm focus:outline-none focus:border-rose-500/60 transition-colors"
                  />
                </div>
                <div>
                  <label className="block text-gray-400 text-xs font-medium mb-1.5 uppercase tracking-wider">Message</label>
                  <textarea
                    name="message" value={form.message} onChange={handleChange}
                    rows={5} placeholder="Your message here..."
                    className="w-full bg-white/5 border border-purple-800/40 rounded-xl px-4 py-3 text-white placeholder-gray-600 text-sm focus:outline-none focus:border-rose-500/60 transition-colors resize-none"
                  />
                </div>
                <button
                  type="submit"
                  className="w-full bg-linear-to-r from-rose-600 to-violet-600 hover:from-rose-500 hover:to-violet-500 text-white font-semibold py-3 rounded-xl transition-all duration-200 text-sm shadow-lg"
                >
                  Send Message →
                </button>
              </form>
            )}
          </div>

          {/* Right panel */}
          <div className="sm:col-span-2 space-y-4">
            <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-5">
              <h3 className="text-white font-semibold mb-3">Get in touch</h3>
              <div className="space-y-3">
                <div className="flex items-center gap-3 text-sm text-gray-400">
                  <span className="text-xl">📧</span>
                  <span>support@vidyaai.in</span>
                </div>
                <div className="flex items-center gap-3 text-sm text-gray-400">
                  <span className="text-xl">⏰</span>
                  <span>Response within 24 hours</span>
                </div>
                <div className="flex items-center gap-3 text-sm text-gray-400">
                  <span className="text-xl">🇮🇳</span>
                  <span>India · Hindi &amp; English</span>
                </div>
              </div>
            </div>

            <div className="bg-[#130022] border border-purple-800/30 rounded-2xl p-5">
              <h3 className="text-white font-semibold mb-3">Follow us</h3>
              <div className="space-y-2">
                {socials.map(s => (
                  <a
                    key={s.label}
                    href={s.href}
                    className={`flex items-center gap-3 px-4 py-2.5 rounded-xl border ${s.bg} ${s.border} ${s.color} text-sm font-medium hover:opacity-80 transition-opacity`}
                  >
                    <span className="text-xl">{s.icon}</span>
                    {s.label}
                  </a>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}
