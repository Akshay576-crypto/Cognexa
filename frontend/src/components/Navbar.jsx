import { ArrowRight, Menu, X } from "lucide-react";
import { useState } from "react";

function Navbar() {
    const [mobileOpen, setMobileOpen] = useState(false);

    const navLinks = [
        { label: "Platform", href: "#platform" },
        { label: "Why Cognexa", href: "#why-cognexa" },
        { label: "Features", href: "#features" },
        { label: "Project Helix", href: "#helix" },
        { label: "Who We Are", href: "#who-we-are" },
        { label: "The Problem", href: "#problem" },
    ];

    return (
        <header className="fixed top-0 left-0 right-0 z-50">
            <nav className="mx-auto mt-4 max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="rounded-2xl border border-white/10 bg-black/60 px-5 py-3 backdrop-blur-xl">
                    <div className="flex items-center justify-between">

                        {/* Logo */}
                        <a href="/" className="flex items-center gap-3">
                            <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-white text-black">
                                <span className="text-lg font-bold">C</span>
                            </div>

                            <span className="text-xl font-semibold tracking-tight text-white">
                                Cognexa
                            </span>
                        </a>

                        {/* Desktop Navigation */}
                        <div className="hidden items-center gap-8 md:flex">
                            {navLinks.map((link) => (
                                <a
                                    key={link.label}
                                    href={link.href}
                                    className="text-sm text-white/60 transition hover:text-white"
                                >
                                    {link.label}
                                </a>
                            ))}
                        </div>

                        {/* Desktop CTA */}
                        <div className="hidden items-center gap-3 md:flex">
                            <a
                                href="/login"
                                className="px-4 py-2 text-sm text-white/70 transition hover:text-white"
                            >
                                Sign In
                            </a>

                            <a
                                href="/register"
                                className="group flex items-center gap-2 rounded-xl bg-white px-4 py-2 text-sm font-medium text-black transition hover:bg-white/90"
                            >
                                Start Using Cognexa
                                <ArrowRight
                                    size={15}
                                    className="transition-transform group-hover:translate-x-0.5"
                                />
                            </a>
                        </div>

                        {/* Mobile Menu Button */}
                        <button
                            onClick={() => setMobileOpen(!mobileOpen)}
                            className="rounded-lg p-2 text-white md:hidden"
                            aria-label="Toggle navigation"
                        >
                            {mobileOpen ? <X size={22} /> : <Menu size={22} />}
                        </button>
                    </div>

                    {/* Mobile Navigation */}
                    {mobileOpen && (
                        <div className="mt-4 border-t border-white/10 pt-4 md:hidden">
                            <div className="flex flex-col gap-4">
                                {navLinks.map((link) => (
                                    <a
                                        key={link.label}
                                        href={link.href}
                                        onClick={() => setMobileOpen(false)}
                                        className="text-sm text-white/70 transition hover:text-white"
                                    >
                                        {link.label}
                                    </a>
                                ))}

                                <a
                                    href="/login"
                                    className="text-sm text-white/70"
                                >
                                    Sign In
                                </a>

                                <a
                                    href="/register"
                                    className="flex items-center justify-center gap-2 rounded-xl bg-white px-4 py-3 text-sm font-medium text-black"
                                >
                                    Start Using Cognexa
                                    <ArrowRight size={15} />
                                </a>
                            </div>
                        </div>
                    )}
                </div>
            </nav>
        </header>
    );
}

export default Navbar;