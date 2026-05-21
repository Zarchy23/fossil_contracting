import Link from 'next/link'
import { Mail, Phone, MapPin, Send, Code, Briefcase, Share2 } from 'lucide-react'

export default function Footer() {
  return (
    <footer className="bg-gradient-to-b from-gray-900 to-gray-950 text-white pt-16 pb-8">
      <div className="container mx-auto px-4">
        <div className="grid md:grid-cols-4 gap-8 mb-12">
          {/* Company Info */}
          <div>
            <div className="mb-4">
              <img
                src="/images/logo.png"
                alt="Fossil Contracting Logo"
                className="h-16 w-auto mb-2"
              />
            </div>
            <p className="text-gray-400 text-sm leading-relaxed">
              Zimbabwe's premium civil contracting company, delivering excellence in infrastructure development since 2000.
            </p>
            <div className="flex gap-3 mt-6">
              <a href="#" className="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-green-600 transition-colors">
                <Send size={18} />
              </a>
              <a href="#" className="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-green-600 transition-colors">
                <Code size={18} />
              </a>
              <a href="#" className="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-green-600 transition-colors">
                <Briefcase size={18} />
              </a>
              <a href="#" className="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-green-600 transition-colors">
                <Share2 size={18} />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-lg font-semibold mb-4 text-green-400">Quick Links</h3>
            <ul className="space-y-2">
              <li><Link href="/about" className="text-gray-400 hover:text-green-400 transition-colors">About Us</Link></li>
              <li><Link href="/services" className="text-gray-400 hover:text-green-400 transition-colors">Our Services</Link></li>
              <li><Link href="/projects" className="text-gray-400 hover:text-green-400 transition-colors">Projects</Link></li>
              <li><Link href="/anonymous-feedback" className="text-gray-400 hover:text-green-400 transition-colors">Anonymous Feedback</Link></li>
              <li><Link href="/community-blog" className="text-gray-400 hover:text-green-400 transition-colors">Community Blog</Link></li>
            </ul>
          </div>

          {/* Services */}
          <div>
            <h3 className="text-lg font-semibold mb-4 text-green-400">Our Services</h3>
            <ul className="space-y-2">
              <li><Link href="/services/road-construction" className="text-gray-400 hover:text-green-400 transition-colors">Road Construction</Link></li>
              <li><Link href="/services/earth-works" className="text-gray-400 hover:text-green-400 transition-colors">Earth Works</Link></li>
              <li><Link href="/services/building-works" className="text-gray-400 hover:text-green-400 transition-colors">Building Works</Link></li>
              <li><Link href="/services/contract-mining" className="text-gray-400 hover:text-green-400 transition-colors">Contract Mining</Link></li>
              <li><Link href="/services/plant-hire" className="text-gray-400 hover:text-green-400 transition-colors">Plant Hire</Link></li>
            </ul>
          </div>

          {/* Contact Info */}
          <div>
            <h3 className="text-lg font-semibold mb-4 text-green-400">Contact Us</h3>
            <ul className="space-y-3">
              <li className="flex items-start gap-3 text-gray-400">
                <MapPin size={18} className="mt-0.5 flex-shrink-0 text-green-400" />
                <span className="text-sm">5 Loreley Close, Beverly Masasa, Harare, Zimbabwe</span>
              </li>
              <li className="flex items-center gap-3 text-gray-400">
                <Phone size={18} className="text-green-400" />
                <span className="text-sm">+263 8677 009771</span>
              </li>
              <li className="flex items-center gap-3 text-gray-400">
                <Mail size={18} className="text-green-400" />
                <span className="text-sm">admin@fossilzim.com</span>
              </li>
            </ul>
            <div className="mt-6 pt-6 border-t border-gray-800">
              <p className="text-gray-500 text-xs text-center">
                © {new Date().getFullYear()} Fossil Contracting. All rights reserved.
              </p>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}
