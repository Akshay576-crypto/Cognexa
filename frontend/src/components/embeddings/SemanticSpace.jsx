import { motion } from "framer-motion";

const points = [
    { x: "18%", y: "28%", label: "research", type: "violet" },
    { x: "27%", y: "43%", label: "analysis", type: "violet" },
    { x: "20%", y: "62%", label: "evidence", type: "violet" },

    { x: "48%", y: "34%", label: "meaning", type: "core" },
    { x: "55%", y: "52%", label: "context", type: "core" },
    { x: "45%", y: "68%", label: "relationship", type: "core" },

    { x: "76%", y: "30%", label: "retrieval", type: "cyan" },
    { x: "83%", y: "48%", label: "query", type: "cyan" },
    { x: "74%", y: "67%", label: "relevance", type: "cyan" },
];

const typeStyles = {
    violet: {
        dot: "bg-violet-300",
        glow: "shadow-[0_0_18px_rgba(167,139,250,0.55)]",
        text: "text-violet-200/50",
    },
    core: {
        dot: "bg-white",
        glow: "shadow-[0_0_22px_rgba(255,255,255,0.5)]",
        text: "text-white/60",
    },
    cyan: {
        dot: "bg-cyan-300",
        glow: "shadow-[0_0_18px_rgba(103,232,249,0.55)]",
        text: "text-cyan-200/50",
    },
};

function SemanticSpace() {
    return (
        <div className="relative h-[420px] w-full overflow-hidden rounded-[34px] border border-white/[0.08] bg-white/[0.018] backdrop-blur-xl">

            {/* Ambient semantic field */}
            <div
                className="
                    pointer-events-none
                    absolute
                    left-[28%]
                    top-[22%]
                    h-[260px]
                    w-[260px]
                    rounded-full
                    bg-violet-400/[0.045]
                    blur-[100px]
                "
            />

            <div
                className="
                    pointer-events-none
                    absolute
                    right-[20%]
                    bottom-[15%]
                    h-[220px]
                    w-[220px]
                    rounded-full
                    bg-cyan-400/[0.035]
                    blur-[100px]
                "
            />

            {/* Grid */}
            <div
                className="
                    pointer-events-none
                    absolute
                    inset-0
                    opacity-[0.12]
                    [background-image:linear-gradient(rgba(255,255,255,0.06)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.06)_1px,transparent_1px)]
                    [background-size:70px_70px]
                "
            />

            {/* Connection field */}
            <svg
                className="pointer-events-none absolute inset-0 h-full w-full"
                viewBox="0 0 1000 420"
                preserveAspectRatio="none"
            >
                <defs>
                    <linearGradient
                        id="semantic-gradient"
                        x1="0%"
                        y1="0%"
                        x2="100%"
                        y2="0%"
                    >
                        <stop
                            offset="0%"
                            stopColor="#a78bfa"
                            stopOpacity="0.08"
                        />
                        <stop
                            offset="50%"
                            stopColor="#ffffff"
                            stopOpacity="0.18"
                        />
                        <stop
                            offset="100%"
                            stopColor="#67e8f9"
                            stopOpacity="0.08"
                        />
                    </linearGradient>
                </defs>

                <path
                    d="M180 118 C320 70 390 150 480 143"
                    fill="none"
                    stroke="url(#semantic-gradient)"
                    strokeWidth="1"
                />

                <path
                    d="M270 180 C360 180 420 210 550 218"
                    fill="none"
                    stroke="url(#semantic-gradient)"
                    strokeWidth="1"
                />

                <path
                    d="M200 260 C330 300 390 260 450 285"
                    fill="none"
                    stroke="url(#semantic-gradient)"
                    strokeWidth="1"
                />

                <path
                    d="M550 145 C650 100 730 120 780 126"
                    fill="none"
                    stroke="url(#semantic-gradient)"
                    strokeWidth="1"
                />

                <path
                    d="M550 218 C650 190 730 195 830 202"
                    fill="none"
                    stroke="url(#semantic-gradient)"
                    strokeWidth="1"
                />

                <path
                    d="M500 285 C620 310 700 280 760 280"
                    fill="none"
                    stroke="url(#semantic-gradient)"
                    strokeWidth="1"
                />
            </svg>

            {/* Field label */}
            <div className="absolute left-6 top-6">
                <p className="text-[8px] uppercase tracking-[0.3em] text-white/20">
                    Semantic space
                </p>

                <p className="mt-2 text-[9px] text-white/15">
                    Meaning represented as relationships
                </p>
            </div>

            {/* Points */}
            {points.map((point, index) => {
                const style = typeStyles[point.type];

                return (
                    <motion.div
                        key={point.label}
                        initial={{
                            opacity: 0,
                            scale: 0.7,
                        }}
                        whileInView={{
                            opacity: 1,
                            scale: 1,
                        }}
                        viewport={{
                            once: true,
                            amount: 0.25,
                        }}
                        transition={{
                            duration: 0.6,
                            delay: index * 0.08,
                        }}
                        className="absolute"
                        style={{
                            left: point.x,
                            top: point.y,
                        }}
                    >
                        <div className="flex -translate-x-1/2 -translate-y-1/2 items-center gap-2">
                            <span
                                className={`
                                    h-2
                                    w-2
                                    rounded-full
                                    ${style.dot}
                                    ${style.glow}
                                `}
                            />

                            <span
                                className={`
                                    whitespace-nowrap
                                    text-[8px]
                                    uppercase
                                    tracking-[0.16em]
                                    ${style.text}
                                `}
                            >
                                {point.label}
                            </span>
                        </div>
                    </motion.div>
                );
            })}

            {/* Central semantic core */}
            <motion.div
                animate={{
                    scale: [1, 1.035, 1],
                    opacity: [0.8, 1, 0.8],
                }}
                transition={{
                    duration: 4,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="
                    absolute
                    left-1/2
                    top-1/2
                    h-16
                    w-16
                    -translate-x-1/2
                    -translate-y-1/2
                    rounded-full
                    border
                    border-white/[0.16]
                    bg-white/[0.035]
                    shadow-[0_0_55px_rgba(255,255,255,0.08)]
                    backdrop-blur-2xl
                "
            >
                <div className="flex h-full items-center justify-center">
                    <span className="text-[7px] uppercase tracking-[0.2em] text-white/45">
                        meaning
                    </span>
                </div>
            </motion.div>

            {/* Bottom legend */}
            <div className="absolute bottom-5 left-6 flex items-center gap-5">
                <div className="flex items-center gap-2">
                    <span className="h-1.5 w-1.5 rounded-full bg-violet-300" />
                    <span className="text-[7px] uppercase tracking-[0.18em] text-white/20">
                        Input concepts
                    </span>
                </div>

                <div className="flex items-center gap-2">
                    <span className="h-1.5 w-1.5 rounded-full bg-cyan-300" />
                    <span className="text-[7px] uppercase tracking-[0.18em] text-white/20">
                        Retrieval concepts
                    </span>
                </div>
            </div>
        </div>
    );
}

export default SemanticSpace;