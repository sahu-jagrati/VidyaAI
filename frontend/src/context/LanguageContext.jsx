import { createContext, useContext, useState } from 'react';
import en from '../translations/en';
import hi from '../translations/hi';

const LanguageContext = createContext(null);

export function LanguageProvider({ children }) {
  const [lang, setLang] = useState(() => localStorage.getItem('vidya_lang') || 'en');

  const switchLang = (l) => {
    setLang(l);
    localStorage.setItem('vidya_lang', l);
  };

  const t = (key) => {
    const dict = lang === 'hi' ? hi : en;
    return dict[key] ?? en[key] ?? key;
  };

  return (
    <LanguageContext.Provider value={{ lang, switchLang, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export const useLang = () => useContext(LanguageContext);
