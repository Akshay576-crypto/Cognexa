import { motion } from "framer-motion";
import { ArrowRight, Database, Search, Sparkles } from "lucide-react";

const stages = [
    {
        id: "hac",
        number: "01",
        label: "HAC",
        title: "Structure information",
        description:
            "Helix Adaptive Chunking preserves the natural structure of documents before information enters the semantic layer.",
        icon: Database,
        accent: "violet",
    },
    {
        id: "embedding",
        number: "02",
        label: "EMBEDDINGS",
        title: "Create semantic meaning",
        description:
            "Structured information becomes numerical representations that capture relationships and meaning.",
        icon: Sparkles,
        accent: "white",
    },
    {
        id: "hare",
        number: "03",
        label: "HARE",
        title: "Retrieve intelligence",
        description:
            "Helix Adaptive Retrieval Engine navigates the semantic space to find the context that matters.",
        icon: Search,
        accent: "cyan",
    },
];

const accentStyles = {
    violet: {
        glow: "bg-violet-400/[0.08]",
        border: "border-violet-300/[0.16]",
        icon: "text-violet-200",
        line: "from-violet-300/0 via-violet-300/60 to-violet-300/0",
    },
    white: {
        glow: "bg-white/[0.055]",
        border: "border-white/[0.14]",
        icon: "text-white",
        line: "from-white/0 via-white/50 to-white/0",
    },
    cyan: {
        glow: "bg-cyan-300/[0.07]",
        border: "border-cyan-300/[0.16]",
        icon: "text-cyan-200",
        line: "from-cyan-300/0 via-cyan-300/60 to-cyan-300/0",
    },
};

function IntelligencePipeline() {
    return (
        <section className="relative overflow-hidden px-6 py-32 sm:px-10 lg:px-16">
            {/* Ambient intelligence field */}
            <motion.div
                animate={{
                    scale: [1, 1.08, 1],
                    opacity: [0.18, 0.28, 0.18],
                }}
                transition={{
                    duration: 10,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="
                    pointer-events-none
                    absolute
                    left-1/2
                    top-1/2
                    h-[500px]
                    w-[900px]
                    -translate-x-1/2
                    -translate-y-1/2
                    rounded-full
                    bg-gradient-to-r
                    from-violet-500/[0.07]
                    via-white/[0.025]
                    to-cyan-400/[0.07]
                    blur-[140px]
                "
            />

            <div className="relative mx-auto max-w-[1250px]">
                {/* Section introduction */}
                <div className="mx-auto max-w-3xl text-center">
                    <motion.div
                        initial={{ opacity: 0, y: 15 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true, amount: 0.4 }}
                        transition={{ duration: 0.7 }}
                        className="
                            inline-flex
                            items-center
                            gap-2
                            rounded-full
                            border
                            border-white/[0.10]
                            bg-white/[0.035]
                            px-3
                            py-1.5
                            text-[9px]
                            uppercase
                            tracking-[0.28em]
                            text-white/45
                            backdrop-blur-xl
                        "
                    >
                        <span className="h-1.5 w-1.5 rounded-full bg-cyan-200/80 shadow-[0_0_12px_rgba(165,243,252,0.8)]" />
                        The Cognexa intelligence layer
                    </motion.div>

                    <motion.h2
                        initial={{ opacity: 0, y: 25 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true, amount: 0.4 }}
                        transition={{ duration: 0.8, delay: 0.1 }}
                        className="
                            mt-7
                            text-4xl
                            font-medium
                            tracking-[-0.055em]
                            text-white
                            sm:text-5xl
                            lg:text-6xl
                        "
                    >
                        Information enters.
                        <br />
                        <span className="text-white/30">
                            Intelligence emerges.
                        </span>
                    </motion.h2>

                    <motion.p
                        initial={{ opacity: 0, y: 15 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true, amount: 0.4 }}
                        transition={{ duration: 0.7, delay: 0.2 }}
                        className="
                            mx-auto
                            mt-6
                            max-w-2xl
                            text-sm
                            leading-7
                            text-white/38
                            sm:text-base
                        "
                    >
                        Cognexa transforms raw information through a continuous
                        intelligence pipeline — preserving structure, encoding
                        meaning, and retrieving the context that matters.
                    </motion.p>
                </div>

                {/* Pipeline */}
                <div className="relative mt-20">
                    {/* Connecting information stream */}
                    <div className="pointer-events-none absolute left-[16%] right-[16%] top-1/2 hidden h-px -translate-y-1/2 lg:block">
                        <div className="absolute inset-0 bg-gradient-to-r from-violet-300/0 via-white/15 to-cyan-300/0" />

                        {[0, 1, 2, 3].map((particle) => (
                            <motion.span
                                key={particle}
                                className="absolute top-1/2 h-1.5 w-1.5 -translate-y-1/2 rounded-full bg-white shadow-[0_0_16px_rgba(255,255,255,0.8)]"
                                animate={{
                                    left: ["0%", "100%"],
                                    opacity: [0, 1, 1, 0],
                                }}
                                transition={{
                                    duration: 4.5,
                                    repeat: Infinity,
                                    delay: particle * 1.1,
                                    ease: "linear",
                                }}
                            />
                        ))}
                    </div>

                    <div className="grid gap-5 lg:grid-cols-3">
                        {stages.map((stage, index) => {
                            const styles = accentStyles[stage.accent];
                            const Icon = stage.icon;

                            return (
                                <motion.div
                                    key={stage.id}
                                    initial={{
                                        opacity: 0,
                                        y: 35,
                                    }}
                                    whileInView={{
                                        opacity: 1,
                                        y: 0,
                                    }}
                                    viewport={{
                                        once: true,
                                        amount: 0.25,
                                    }}
                                    transition={{
                                        duration: 0.75,
                                        delay: index * 0.15,
                                    }}
                                    className="relative"
                                >
                                    <div
                                        className={`
                                            relative
                                            min-h-[310px]
                                            overflow-hidden
                                            rounded-[32px]
                                            border
                                            ${styles.border}
                                            ${styles.glow}
                                            p-7
                                            backdrop-blur-[35px]
                                            transition-transform
                                            duration-500
                                            hover:-translate-y-2
                                        `}
                                    >
                                        {/* Glass reflection */}
                                        <div
                                            className="
                                                pointer-events-none
                                                absolute
                                                inset-x-8
                                                top-0
                                                h-px
                                                bg-gradient-to-r
                                                from-transparent
                                                via-white/30
                                                to-transparent
                                            "
                                        />

                                        {/* Ambient glow */}
                                        <div
                                            className={`
                                                pointer-events-none
                                                absolute
                                                -right-20
                                                -top-20
                                                h-48
                                                w-48
                                                rounded-full
                                                ${styles.glow}
                                                blur-[70px]
                                            `}
                                        />

                                        {/* Header */}
                                        <div className="relative z-10 flex items-center justify-between">
                                            <span className="text-[9px] font-medium tracking-[0.25em] text-white/25">
                                                {stage.number}
                                            </span>

                                            <Icon
                                                size={17}
                                                strokeWidth={1.5}
                                                className={styles.icon}
                                            />
                                        </div>

                                        {/* Core */}
                                        <div className="relative z-10 mt-12">
                                            <div className="flex items-center gap-3">
                                                <div
                                                    className={`
                                                        h-2
                                                        w-2
                                                        rounded-full
                                                        ${styles.icon.replace(
                                                        "text-",
                                                        "bg-",
                                                    )}
                                                        shadow-[0_0_15px_currentColor]
                                                    `}
                                                />

                                                <span className="text-[10px] uppercase tracking-[0.25em] text-white/45">
                                                    {stage.label}
                                                </span>
                                            </div>

                                            <h3 className="mt-5 text-2xl font-medium tracking-[-0.04em] text-white/90">
                                                {stage.title}
                                            </h3>

                                            <p className="mt-4 text-sm leading-6 text-white/35">
                                                {stage.description}
                                            </p>
                                        </div>

                                        {/* Bottom system indicator */}
                                        <div className="absolute bottom-6 left-7 right-7 flex items-center justify-between">
                                            <span className="text-[8px] uppercase tracking-[0.2em] text-white/20">
                                                Helix layer
                                            </span>

                                            <span className="h-px w-12 bg-gradient-to-r from-transparent via-white/20 to-transparent" />
                                        </div>
                                    </div>

                                    {/* Desktop transition indicator */}
                                    {index < stages.length - 1 && (
                                        <div className="absolute -right-4 top-1/2 z-20 hidden -translate-y-1/2 lg:block">
                                            <ArrowRight
                                                size={14}
                                                strokeWidth={1}
                                                className="text-white/20"
                                            />
                                        </div>
                                    )}
                                </motion.div>
                            );
                        })}
                    </div>
                </div>

                {/* Bottom statement */}
                <motion.div
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 1, delay: 0.3 }}
                    className="mt-12 text-center"
                >
                    <span className="text-[9px] uppercase tracking-[0.35em] text-white/20">
                        HAC → Semantic Representation → HARE
                    </span>
                </motion.div>
            </div>
        </section>
    );
}

export default IntelligencePipeline;