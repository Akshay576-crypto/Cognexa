import { ArrowRight, Sparkles } from "lucide-react";
import { motion } from "framer-motion";

function Hero() {
    return (
        <section className="relative flex min-h-screen items-center overflow-hidden bg-black pt-28">

            {/* Aurora Background */}
            <div className="pointer-events-none absolute inset-0">
                <div className="absolute left-1/2 top-1/4 h-[500px] w-[500px] -translate-x-1/2 rounded-full bg-indigo-500/10 blur-[140px]" />
                <div className="absolute right-0 top-1/3 h-[400px] w-[400px] rounded-full bg-cyan-400/10 blur-[140px]" />
                <div className="absolute bottom-0 left-0 h-[350px] w-[350px] rounded-full bg-violet-500/10 blur-[140px]" />
            </div>

            {/* Subtle Grid */}
            <div
                className="pointer-events-none absolute inset-0 opacity-[0.035]"
                style={{
                    backgroundImage:
                        "linear-gradient(rgba(255,255,255,1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,1) 1px, transparent 1px)",
                    backgroundSize: "60px 60px",
                }}
            />

            <div className="relative mx-auto grid w-full max-w-7xl items-center gap-16 px-6 py-20 lg:grid-cols-2 lg:px-8">

                {/* Left Content */}
                <motion.div
                    initial={{ opacity: 0, y: 25 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.7 }}
                >
                    {/* Badge */}
                    <div className="mb-7 inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/[0.04] px-4 py-2 text-sm text-white/70 backdrop-blur-md">
                        <Sparkles size={15} className="text-white" />
                        Enterprise AI Intelligence Platform
                    </div>

                    {/* Heading */}
                    <h1 className="max-w-4xl text-5xl font-semibold tracking-[-0.04em] text-white sm:text-6xl lg:text-7xl">
                        Intelligence for the{" "}
                        <span className="bg-gradient-to-r from-white via-white/80 to-white/40 bg-clip-text text-transparent">
                            information-driven enterprise.
                        </span>
                    </h1>

                    {/* Description */}
                    <p className="mt-7 max-w-2xl text-lg leading-8 text-white/55 sm:text-xl">
                        Cognexa brings research, knowledge, analysis, and intelligent
                        automation together in one enterprise AI platform — helping
                        organizations turn complex information into meaningful decisions.
                    </p>

                    {/* CTA */}
                    <div className="mt-9 flex flex-col gap-4 sm:flex-row">
                        <a
                            href="/register"
                            className="group inline-flex items-center justify-center gap-2 rounded-xl bg-white px-6 py-3.5 font-medium text-black transition hover:bg-white/90"
                        >
                            Start Using Cognexa
                            <ArrowRight
                                size={17}
                                className="transition-transform group-hover:translate-x-1"
                            />
                        </a>

                        <a
                            href="#platform"
                            className="inline-flex items-center justify-center rounded-xl border border-white/10 bg-white/[0.03] px-6 py-3.5 font-medium text-white/80 backdrop-blur-md transition hover:bg-white/[0.07] hover:text-white"
                        >
                            Explore Platform
                        </a>
                    </div>

                    {/* Trust statement */}
                    <div className="mt-10 flex items-center gap-3 text-sm text-white/35">
                        <div className="h-px w-8 bg-white/20" />
                        Built for intelligent, information-driven work
                    </div>
                </motion.div>

                {/* Right Intelligence Visual */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.92 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 0.9, delay: 0.15 }}
                    className="relative hidden min-h-[500px] items-center justify-center lg:flex"
                >
                    {/* Outer Glow */}
                    <div className="absolute h-[340px] w-[340px] rounded-full bg-cyan-400/10 blur-[100px]" />

                    {/* Core */}
                    <motion.div
                        animate={{
                            scale: [1, 1.04, 1],
                        }}
                        transition={{
                            duration: 5,
                            repeat: Infinity,
                            ease: "easeInOut",
                        }}
                        className="relative flex h-64 w-64 items-center justify-center rounded-full border border-white/15 bg-white/[0.035] shadow-2xl backdrop-blur-xl"
                    >
                        <div className="absolute inset-8 rounded-full border border-white/10" />

                        <div className="flex h-28 w-28 items-center justify-center rounded-full border border-white/20 bg-white/[0.07] shadow-[0_0_80px_rgba(255,255,255,0.08)]">
                            <span className="text-4xl font-semibold text-white">C</span>
                        </div>
                    </motion.div>

                    {/* Floating Nodes */}
                    <div className="absolute left-8 top-20 rounded-xl border border-white/10 bg-white/[0.04] px-4 py-3 backdrop-blur-xl">
                        <p className="text-xs text-white/35">KNOWLEDGE</p>
                        <p className="mt-1 text-sm text-white/80">Documents</p>
                    </div>

                    <div className="absolute right-4 top-32 rounded-xl border border-white/10 bg-white/[0.04] px-4 py-3 backdrop-blur-xl">
                        <p className="text-xs text-white/35">INTELLIGENCE</p>
                        <p className="mt-1 text-sm text-white/80">Research</p>
                    </div>

                    <div className="absolute bottom-20 left-16 rounded-xl border border-white/10 bg-white/[0.04] px-4 py-3 backdrop-blur-xl">
                        <p className="text-xs text-white/35">OUTPUT</p>
                        <p className="mt-1 text-sm text-white/80">Insights</p>
                    </div>

                    <div className="absolute bottom-12 right-12 rounded-xl border border-white/10 bg-white/[0.04] px-4 py-3 backdrop-blur-xl">
                        <p className="text-xs text-white/35">ACTION</p>
                        <p className="mt-1 text-sm text-white/80">Decisions</p>
                    </div>
                </motion.div>
            </div>
        </section>
    );
}

export default Hero;