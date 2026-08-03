import {
    AlertCircle,
    FileSearch,
    Layers,
    Search,
    ShieldCheck,
} from "lucide-react";
import { motion } from "framer-motion";

function Problem() {
    const problems = [
        {
            icon: Layers,
            title: "Information is fragmented",
            description:
                "Critical knowledge is spread across PDFs, reports, documents, databases, and external sources.",
        },
        {
            icon: Search,
            title: "Research takes too long",
            description:
                "Teams spend hours searching, reading, comparing, and organizing information before they can reach a conclusion.",
        },
        {
            icon: AlertCircle,
            title: "Answers aren't always enough",
            description:
                "An AI-generated response can sound convincing while lacking sufficient evidence, context, or supporting sources.",
        },
        {
            icon: FileSearch,
            title: "Understanding requires context",
            description:
                "Finding a relevant passage is only the beginning. Real intelligence requires understanding the surrounding information and relationships.",
        },
    ];

    return (
        <section
            id="problem"
            className="relative overflow-hidden bg-black px-6 py-32 sm:py-40"
        >
            {/* Background */}
            <div className="pointer-events-none absolute right-0 top-1/4 h-[500px] w-[500px] rounded-full bg-red-500/[0.035] blur-[150px]" />

            <div className="relative mx-auto max-w-7xl">

                {/* Heading */}
                <motion.div
                    initial={{ opacity: 0, y: 25 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.3 }}
                    transition={{ duration: 0.7 }}
                    className="max-w-4xl"
                >
                    <p className="text-sm font-medium uppercase tracking-[0.25em] text-white/35">
                        The Problem
                    </p>

                    <h2 className="mt-5 text-4xl font-semibold tracking-[-0.035em] text-white sm:text-5xl lg:text-6xl">
                        Information is everywhere.
                        <br />
                        <span className="text-white/40">
                            Reliable intelligence isn't.
                        </span>
                    </h2>

                    <p className="mt-7 max-w-2xl text-lg leading-8 text-white/50">
                        Organizations have more information than ever. But turning that
                        information into trustworthy research, meaningful analysis, and
                        confident decisions remains difficult.
                    </p>
                </motion.div>

                {/* Problem cards */}
                <div className="mt-20 grid gap-px overflow-hidden rounded-3xl border border-white/10 bg-white/10 sm:grid-cols-2">
                    {problems.map((problem, index) => {
                        const Icon = problem.icon;

                        return (
                            <motion.div
                                key={problem.title}
                                initial={{ opacity: 0, y: 20 }}
                                whileInView={{ opacity: 1, y: 0 }}
                                viewport={{ once: true }}
                                transition={{
                                    duration: 0.6,
                                    delay: index * 0.08,
                                }}
                                className="group bg-black p-8 transition hover:bg-white/[0.025] sm:p-10"
                            >
                                <div className="flex h-11 w-11 items-center justify-center rounded-xl border border-white/10 bg-white/[0.04]">
                                    <Icon
                                        size={20}
                                        className="text-white/60 transition group-hover:text-white"
                                    />
                                </div>

                                <h3 className="mt-7 text-xl font-semibold text-white">
                                    {problem.title}
                                </h3>

                                <p className="mt-3 max-w-md leading-7 text-white/40">
                                    {problem.description}
                                </p>
                            </motion.div>
                        );
                    })}
                </div>

                {/* Trust problem */}
                <motion.div
                    initial={{ opacity: 0, y: 25 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.7 }}
                    className="relative mt-20 overflow-hidden rounded-3xl border border-white/10 bg-white/[0.025] p-8 sm:p-12"
                >
                    <div className="absolute right-0 top-0 h-64 w-64 rounded-full bg-white/[0.025] blur-[100px]" />

                    <div className="relative grid gap-10 lg:grid-cols-[1fr_auto] lg:items-center">

                        <div>
                            <div className="flex items-center gap-3">
                                <ShieldCheck size={21} className="text-white/60" />

                                <span className="text-sm font-medium uppercase tracking-[0.2em] text-white/40">
                                    The real challenge
                                </span>
                            </div>

                            <h3 className="mt-5 max-w-3xl text-3xl font-semibold tracking-tight text-white sm:text-4xl">
                                The question isn't just{" "}
                                <span className="text-white/40">
                                    “Can AI answer?”
                                </span>
                                <br />
                                It's{" "}
                                <span className="text-white">
                                    “Can we understand and validate the answer?”
                                </span>
                            </h3>
                        </div>

                        {/* Visual */}
                        <div className="flex h-32 w-32 shrink-0 items-center justify-center rounded-full border border-white/10 bg-white/[0.025]">
                            <div className="flex h-20 w-20 items-center justify-center rounded-full border border-white/10 bg-white/[0.04]">
                                <ShieldCheck size={28} className="text-white/50" />
                            </div>
                        </div>
                    </div>
                </motion.div>

                {/* Bottom transition */}
                <motion.div
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8 }}
                    className="mt-16 flex flex-col gap-4 border-t border-white/10 pt-8 sm:flex-row sm:items-center sm:justify-between"
                >
                    <p className="max-w-xl text-base leading-7 text-white/35">
                        Cognexa is built to bridge the gap between raw information,
                        AI-generated answers, and trustworthy decision-making.
                    </p>

                    <span className="text-sm font-medium text-white/50">
                        Information → Understanding → Validation
                    </span>
                </motion.div>
            </div>
        </section>
    );
}

export default Problem;