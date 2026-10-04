import { motion } from "framer-motion";

const stages = [
    {
        label: "HAC chunks",
        sub: "Structured context",
        accent: "violet",
    },
    {
        label: "Encoding",
        sub: "Meaning extraction",
        accent: "white",
    },
    {
        label: "Vectors",
        sub: "Semantic representation",
        accent: "cyan",
    },
];

const accentStyles = {
    violet: {
        border: "border-violet-300/20",
        dot: "bg-violet-300",
        glow: "shadow-[0_0_18px_rgba(167,139,250,0.35)]",
        text: "text-violet-200/60",
    },
    white: {
        border: "border-white/15",
        dot: "bg-white",
        glow: "shadow-[0_0_18px_rgba(255,255,255,0.3)]",
        text: "text-white/50",
    },
    cyan: {
        border: "border-cyan-300/20",
        dot: "bg-cyan-300",
        glow: "shadow-[0_0_18px_rgba(103,232,249,0.35)]",
        text: "text-cyan-200/60",
    },
};

function EmbeddingFlow() {
    return (
        <div className="relative w-full overflow-hidden rounded-[34px] border border-white/[0.08] bg-white/[0.018] px-6 py-8 backdrop-blur-xl">

            {/* Top reflection */}
            <div
                className="
                    pointer-events-none
                    absolute
                    inset-x-[12%]
                    top-0
                    h-px
                    bg-gradient-to-r
                    from-transparent
                    via-white/20
                    to-transparent
                "
            />

            <div className="relative flex flex-col items-center justify-between gap-7 md:flex-row md:gap-5">

                {stages.map((stage, index) => {
                    const style = accentStyles[stage.accent];

                    return (
                        <div
                            key={stage.label}
                            className="flex w-full items-center md:w-auto"
                        >
                            <motion.div
                                initial={{
                                    opacity: 0,
                                    y: 12,
                                }}
                                whileInView={{
                                    opacity: 1,
                                    y: 0,
                                }}
                                viewport={{
                                    once: true,
                                    amount: 0.4,
                                }}
                                transition={{
                                    duration: 0.55,
                                    delay: index * 0.12,
                                }}
                                className={`
                                    relative
                                    min-w-[190px]
                                    rounded-[22px]
                                    border
                                    ${style.border}
                                    bg-white/[0.025]
                                    px-5
                                    py-5
                                    backdrop-blur-xl
                                    ${style.glow}
                                `}
                            >
                                <div className="flex items-center gap-3">
                                    <span
                                        className={`
                                            h-2
                                            w-2
                                            rounded-full
                                            ${style.dot}
                                        `}
                                    />

                                    <span className="text-xs font-medium text-white/75">
                                        {stage.label}
                                    </span>
                                </div>

                                <p
                                    className={`
                                        mt-2
                                        text-[8px]
                                        uppercase
                                        tracking-[0.18em]
                                        ${style.text}
                                    `}
                                >
                                    {stage.sub}
                                </p>

                                {/* Reflection */}
                                <span
                                    className="
                                        pointer-events-none
                                        absolute
                                        inset-x-5
                                        top-0
                                        h-px
                                        bg-gradient-to-r
                                        from-transparent
                                        via-white/20
                                        to-transparent
                                    "
                                />
                            </motion.div>

                            {/* Connector */}
                            {index < stages.length - 1 && (
                                <div className="mx-4 hidden h-px w-14 bg-gradient-to-r from-white/[0.05] via-white/[0.18] to-white/[0.05] md:block">
                                    <motion.div
                                        animate={{
                                            x: ["0%", "100%"],
                                            opacity: [0, 1, 0],
                                        }}
                                        transition={{
                                            duration: 2.8,
                                            repeat: Infinity,
                                            delay: index * 0.8,
                                            ease: "easeInOut",
                                        }}
                                        className="h-px w-5 bg-white/50"
                                    />
                                </div>
                            )}
                        </div>
                    );
                })}
            </div>

            {/* Mobile connectors */}
            <div className="mt-5 flex flex-col items-center gap-2 md:hidden">
                <span className="h-5 w-px bg-white/10" />
                <span className="text-[7px] uppercase tracking-[0.25em] text-white/20">
                    Meaning encoded
                </span>
            </div>

            {/* Status */}
            <div className="mt-7 flex items-center justify-between border-t border-white/[0.05] pt-4">
                <span className="text-[8px] uppercase tracking-[0.25em] text-white/20">
                    Embedding pipeline
                </span>

                <span className="flex items-center gap-2 text-[8px] uppercase tracking-[0.2em] text-white/25">
                    <span className="h-1.5 w-1.5 rounded-full bg-cyan-300/70 shadow-[0_0_10px_rgba(103,232,249,0.5)]" />
                    Semantic representation
                </span>
            </div>
        </div>
    );
}

export default EmbeddingFlow;