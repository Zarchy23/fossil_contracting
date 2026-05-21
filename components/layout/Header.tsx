'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'
import Image from 'next/image'
import { usePathname } from 'next/navigation'
import { Menu, X, Phone, MessageCircle } from 'lucide-react'

const navigation = [
  { name: 'Home', href: '/' },
  { name: 'About', href: '/about' },
  { name: 'Services', href: '/services' },
  { name: 'Projects', href: '/projects' },
  { name: 'Feedback', href: '/anonymous-feedback' },
  { name: 'Community', href: '/community-blog' },
  { name: 'Contact', href: '/contact' },
]

export default function Header() {
  const [isOpen, setIsOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)
  const pathname = usePathname()

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <header className={`fixed top-0 w-full z-50 transition-all duration-500 ${
      scrolled ? 'bg-white/95 backdrop-blur-md shadow-lg' : 'bg-transparent'
    }`}>
      <nav className="container mx-auto px-4 py-4">
        <div className="flex justify-between items-center">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2 group hover:scale-105 transition-transform">
            <Image
              src="/images/logo.png"
              alt="Fossil Contracting Logo"
              width={120}
              height={50}
              className="h-12 w-auto"
              priority
            />
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden lg:flex items-center gap-8">
            {navigation.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className={`${
                  scrolled ? 'text-gray-700' : 'text-white'
                } hover:text-green-500 transition-all duration-300 font-medium ${
                  pathname === item.href ? 'text-green-600 border-b-2 border-green-600' : ''
                }`}
              >
                {item.name}
              </Link>
            ))}
          </div>

          {/* Desktop CTA Button */}
          <div className="hidden lg:flex items-center gap-3">
            <Link
              href="/contact"
              className="bg-green-600 hover:bg-green-700 text-white px-5 py-2 rounded-full text-sm font-semibold transition-all duration-300 hover:scale-105"
            >
              Get a Quote
            </Link>
            <Link
              href="/anonymous-feedback"
              className="bg-white/10 backdrop-blur-sm hover:bg-white/20 text-white px-5 py-2 rounded-full text-sm font-semibold transition-all duration-300 border border-white/30"
            >
              <MessageCircle size={18} className="inline mr-1" />
              Feedback
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className={`lg:hidden p-2 rounded-lg transition-all ${
              scrolled ? 'text-green-800' : 'text-white'
            }`}
          >
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <div className="lg:hidden absolute top-full left-0 right-0 bg-white shadow-xl rounded-b-2xl mt-1 mx-4">
            <div className="flex flex-col p-4">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  onClick={() => setIsOpen(false)}
                  className={`py-3 px-4 text-gray-700 hover:bg-green-50 hover:text-green-600 rounded-xl transition-all ${
                    pathname === item.href ? 'text-green-600 bg-green-50 font-semibold' : ''
                  }`}
                >
                  {item.name}
                </Link>
              ))}
              <div className="border-t border-gray-200 mt-2 pt-4 flex gap-3">
                <Link
                  href="/contact"
                  onClick={() => setIsOpen(false)}
                  className="flex-1 bg-green-600 text-white text-center py-3 rounded-xl font-semibold"
                >
                  Get a Quote
                </Link>
                <Link
                  href="/anonymous-feedback"
                  onClick={() => setIsOpen(false)}
                  className="flex-1 border border-green-600 text-green-600 text-center py-3 rounded-xl font-semibold"
                >
                  Feedback
                </Link>
              </div>
            </div>
          </div>
        )}
      </nav>
    </header>
  )
}
