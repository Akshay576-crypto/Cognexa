import { motion } from "framer-motion";

const chunks = [
    {
        title: "Context",
        text: "Introduction + purpose",
        accent: "violet",
    },
    {
        title: "Method",
        text: "Methodology + data",
        accent: "white",
    },
    {
        title: "Evidence",
        text: "Results + relationships",
        accent: "cyan",
    },
];

const accentStyles = {
    violet: {
        border: "border-violet-300/[0.14]",
        glow: "bg-violet-400/[0.07]",
        dot: "bg-violet-300",
    },
    white: {
        border: "border-white/[0.12]",
        glow: "bg-white/[0.045]",
        dot: "bg-white",
    },
    cyan: {
        border: "border-cyan-300/[0.14]",
        glow: "bg-cyan-400/[0.06]",
        dot: "bg-cyan-300",
    },
};

function HACFlow() {
    return (
        <div className="relative flex w-full flex-col items-center justify-center py-8 lg:min-h-[430px]">

            {/* Central HAC indicator */}
            <motion.div
                initial={{ opacity: 0, scale: 0.8 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true, amount: 0.3 }}
                transition={{
                    duration: 0.8,
                    delay: 0.2,
                }}
                className="
                    relative
                    z-20
                    flex
                    h-24
                    w-24
                    items-center
                    justify-center
                    rounded-full
                    border
                    border-violet-200/[0.16]
                    bg-white/[0.035]
                    shadow-[0_0_70px_rgba(167,139,250,0.12),inset_0_1px_1px_rgba(255,255,255,0.15)]
                    backdrop-blur-2xl
                "
            >
                {/* Outer pulse */}
                <motion.div
                    animate={{
                        scale: [1, 1.35, 1],
                        opacity: [0.3, 0, 0.3],
                    }}
                    transition={{
                        duration: 3,
                        repeat: Infinity,
                        ease: "easeOut",
                    }}
                    className="
                        absolute
                        inset-0
                        rounded-full
                        border
                        border-violet-300/20
                    "
                />

                <div className="text-center">
                    <div className="text-[10px] uppercase tracking-[0.28em] text-violet-200/70">
                        HAC
                    </div>

                    <div className="mt-1 text-[7px] uppercase tracking-[0.16em] text-white/25">
                        Understanding
                    </div>
                </div>
            </motion.div>

            {/* Input → HAC line */}
            <div className="relative h-20 w-full max-w-[700px]">

                <div
                    className="
                        absolute
                        left-1/2
                        top-0
                        h-full
                        w-px
                        -translate-x-1/2
                        bg-gradient-to-b
                        from-white/[0.02]
                        via-violet-300/20
                        to-violet-300/30
                    "
                />

                <motion.div
                    animate={{
                        y: ["0%", "100%"],
                        opacity: [0, 1, 0],
                    }}
                    transition={{
                        duration: 2.2,
                        repeat: Infinity,
                        ease: "linear",
                    }}
                    className="
                        absolute
                        left-1/2
                        top-0
                        h-2
                        w-2
                        -translate-x-1/2
                        rounded-full
                        bg-violet-200
                        shadow-[0_0_15px_rgba(221,214,254,0.9)]
                    "
                />
            </div>

            {/* Output chunks */}
            <div className="grid w-full max-w-[760px] gap-4 md:grid-cols-3">
                {chunks.map((chunk, index) => {
                    const style = accentStyles[chunk.accent];

                    return (
                        <motion.div
                            key={chunk.title}
                            initial={{
                                opacity: 0,
                                y: 25,
                                scale: 0.95,
                            }}
                            whileInView={{
                                opacity: 1,
                                y: 0,
                                scale: 1,
                            }}
                            viewport={{
                                once: true,
                                amount: 0.25,
                            }}
                            transition={{
                                duration: 0.7,
                                delay: 0.5 + index * 0.15,
                            }}
                            className={`
                                relative
                                overflow-hidden
                                rounded-[24px]
                                border
                                ${style.border}
                                ${style.glow}
                                p-5
                                backdrop-blur-2xl
                            `}
                        >
                            {/* Top reflection */}
                            <div
                                className="
                                    absolute
                                    inset-x-5
                                    top-0
                                    h-px
                                    bg-gradient-to-r
                                    from-transparent
                                    via-white/25
                                    to-transparent
                                "
                            />

                            {/* Chunk indicator */}
                            <div className="flex items-center justify-between">
                                <span className="text-[8px] uppercase tracking-[0.22em] text-white/20">
                                    Chunk {String(index + 1).padStart(2, "0")}
                                </span>

                                <span
                                    className={`h-1.5 w-1.5 rounded-full ${style.dot} shadow-[0_0_12px_currentColor]`}
                                />
                            </div>

                            <h4 className="mt-6 text-sm font-medium text-white/75">
                                {chunk.title}
                            </h4>

                            <p className="mt-2 text-[10px] leading-5 text-white/30">
                                {chunk.text}
                            </p>

                            <div className="mt-5 h-px bg-white/[0.05]" />

                            <p className="mt-3 text-[7px] uppercase tracking-[0.18em] text-white/15">
                                Structure preserved
                            </p>
                        </motion.div>
                    );
                })}
            </div>

            {/* Semantic transition */}
            <motion.div
                initial={{ opacity: 0, y: 10 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{
                    duration: 0.7,
                    delay: 0.9,
                }}
                className="mt-8 flex flex-col items-center gap-2"
            >
                <div className="h-8 w-px bg-gradient-to-b from-cyan-300/20 to-transparent" />

                <span className="text-[8px] uppercase tracking-[0.28em] text-white/20">
                    Ready for semantic representation
                </span>
            </motion.div>
        </div>
    );
}

export default HACFlow;