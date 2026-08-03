import { ArrowUpRight, Brain, Layers3, Sparkles } from "lucide-react";
import { motion } from "framer-motion";

function WhoWeAre() {
    return (
        <section
            id="who-we-are"
            className="relative overflow-hidden bg-black px-6 py-28 sm:py-36"
        >
            {/* Background glow */}
            <div className="pointer-events-none absolute left-1/4 top-1/3 h-[400px] w-[400px] rounded-full bg-indigo-500/[0.06] blur-[140px]" />

            <div className="relative mx-auto max-w-7xl">

                {/* Section heading */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.3 }}
                    transition={{ duration: 0.7 }}
                    className="max-w-3xl"
                >
                    <p className="text-sm font-medium uppercase tracking-[0.25em] text-white/40">
                        Who We Are
                    </p>

                    <h2 className="mt-5 text-4xl font-semibold tracking-[-0.03em] text-white sm:text-5xl lg:text-6xl">
                        Building the intelligent layer between{" "}
                        <span className="text-white/45">
                            information and decisions.
                        </span>
                    </h2>

                    <p className="mt-7 max-w-2xl text-lg leading-8 text-white/50">
                        Cognexa is an all-in-one enterprise AI platform designed to help
                        organizations understand information, conduct intelligent
                        research, generate insights, and transform knowledge into action.
                    </p>
                </motion.div>

                {/* Main content */}
                <div className="mt-20 grid gap-6 lg:grid-cols-3">

                    {/* Card 1 */}
                    <motion.div
                        initial={{ opacity: 0, y: 25 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.6 }}
                        className="group rounded-3xl border border-white/10 bg-white/[0.025] p-8 backdrop-blur-xl transition hover:border-white/20"
                    >
                        <div className="flex h-12 w-12 items-center justify-center rounded-2xl border border-white/10 bg-white/[0.05]">
                            <Brain size={22} className="text-white/80" />
                        </div>

                        <h3 className="mt-8 text-xl font-semibold text-white">
                            Intelligence
                        </h3>

                        <p className="mt-4 leading-7 text-white/45">
                            Go beyond retrieving information. Cognexa is designed to
                            understand context, connect knowledge, and produce meaningful
                            intelligence.
                        </p>

                        <ArrowUpRight
                            size={20}
                            className="mt-8 text-white/25 transition group-hover:-translate-y-1 group-hover:translate-x-1 group-hover:text-white/70"
                        />
                    </motion.div>

                    {/* Card 2 */}
                    <motion.div
                        initial={{ opacity: 0, y: 25 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.6, delay: 0.1 }}
                        className="group rounded-3xl border border-white/10 bg-white/[0.025] p-8 backdrop-blur-xl transition hover:border-white/20"
                    >
                        <div className="flex h-12 w-12 items-center justify-center rounded-2xl border border-white/10 bg-white/[0.05]">
                            <Layers3 size={22} className="text-white/80" />
                        </div>

                        <h3 className="mt-8 text-xl font-semibold text-white">
                            One Platform
                        </h3>

                        <p className="mt-4 leading-7 text-white/45">
                            Research, enterprise knowledge, retrieval, analysis, and
                            intelligent content generation come together inside one
                            connected ecosystem.
                        </p>

                        <ArrowUpRight
                            size={20}
                            className="mt-8 text-white/25 transition group-hover:-translate-y-1 group-hover:translate-x-1 group-hover:text-white/70"
                        />
                    </motion.div>

                    {/* Card 3 */}
                    <motion.div
                        initial={{ opacity: 0, y: 25 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.6, delay: 0.2 }}
                        className="group rounded-3xl border border-white/10 bg-white/[0.025] p-8 backdrop-blur-xl transition hover:border-white/20"
                    >
                        <div className="flex h-12 w-12 items-center justify-center rounded-2xl border border-white/10 bg-white/[0.05]">
                            <Sparkles size={22} className="text-white/80" />
                        </div>

                        <h3 className="mt-8 text-xl font-semibold text-white">
                            Built for What Comes Next
                        </h3>

                        <p className="mt-4 leading-7 text-white/45">
                            Cognexa is being built as an evolving intelligence platform,
                            from today's research capabilities toward tomorrow's foundation
                            models and autonomous workflows.
                        </p>

                        <ArrowUpRight
                            size={20}
                            className="mt-8 text-white/25 transition group-hover:-translate-y-1 group-hover:translate-x-1 group-hover:text-white/70"
                        />
                    </motion.div>
                </div>

                {/* Bottom statement */}
                <motion.div
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8 }}
                    className="mt-20 border-t border-white/10 pt-8"
                >
                    <div className="flex flex-col justify-between gap-5 sm:flex-row sm:items-center">
                        <p className="max-w-2xl text-base leading-7 text-white/40">
                            We believe the future of enterprise AI is not simply about
                            generating answers. It is about creating systems that can
                            understand, investigate, and transform knowledge into action.
                        </p>

                        <span className="whitespace-nowrap text-sm font-medium text-white/50">
                            Information → Intelligence → Action
                        </span>
                    </div>
                </motion.div>
            </div>
        </section>
    );
}

export default WhoWeAre;