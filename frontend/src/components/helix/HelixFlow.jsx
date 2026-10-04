import { motion } from "framer-motion";

const nodes = [
    {
        id: "documents",
        label: "Documents",
        sub: "Raw information",
        x: "8%",
        y: "50%",
        tone: "silver",
    },
    {
        id: "hac",
        label: "HAC",
        sub: "Adaptive chunking",
        x: "28%",
        y: "22%",
        tone: "lavender",
    },
    {
        id: "embedding",
        label: "Embeddings",
        sub: "Semantic representation",
        x: "50%",
        y: "50%",
        tone: "white",
    },
    {
        id: "vector",
        label: "Vector Space",
        sub: "Meaning encoded",
        x: "72%",
        y: "22%",
        tone: "ice",
    },
    {
        id: "hare",
        label: "HARE",
        sub: "Adaptive retrieval",
        x: "92%",
        y: "50%",
        tone: "silver",
    },
];

const toneMap = {
    silver: {
        border: "border-white/[0.13]",
        glow: "shadow-[0_0_35px_rgba(255,255,255,0.07)]",
        dot: "bg-[#d9dce3]",
        text: "text-[#d9dce3]",
    },

    lavender: {
        border: "border-[#c8bfff]/[0.18]",
        glow: "shadow-[0_0_35px_rgba(200,191,255,0.08)]",
        dot: "bg-[#c8bfff]",
        text: "text-[#c8bfff]",
    },

    white: {
        border: "border-white/[0.20]",
        glow: "shadow-[0_0_40px_rgba(255,255,255,0.10)]",
        dot: "bg-white",
        text: "text-white",
    },

    ice: {
        border: "border-[#b9eaf2]/[0.16]",
        glow: "shadow-[0_0_35px_rgba(185,234,242,0.07)]",
        dot: "bg-[#b9eaf2]",
        text: "text-[#b9eaf2]",
    },
};

function HelixFlow() {
    return (
        <div className="relative h-[340px] w-full min-w-[720px]">

            {/* Information pathways */}
            <svg
                className="pointer-events-none absolute inset-0 h-full w-full"
                viewBox="0 0 1000 340"
                preserveAspectRatio="none"
            >
                <defs>

                    <linearGradient
                        id="helix-flow"
                        x1="0%"
                        y1="0%"
                        x2="100%"
                        y2="0%"
                    >
                        <stop
                            offset="0%"
                            stopColor="#ffffff"
                            stopOpacity="0.10"
                        />

                        <stop
                            offset="45%"
                            stopColor="#ffffff"
                            stopOpacity="0.32"
                        />

                        <stop
                            offset="70%"
                            stopColor="#c8bfff"
                            stopOpacity="0.16"
                        />

                        <stop
                            offset="100%"
                            stopColor="#ffffff"
                            stopOpacity="0.10"
                        />
                    </linearGradient>

                </defs>

                <path
                    d="M80 170 C180 170 170 75 280 75 S400 170 500 170 S620 75 720 75 S820 170 920 170"
                    fill="none"
                    stroke="url(#helix-flow)"
                    strokeWidth="1"
                />

                <path
                    d="M80 170 C180 170 170 265 280 265 S400 170 500 170 S620 265 720 265 S820 170 920 170"
                    fill="none"
                    stroke="url(#helix-flow)"
                    strokeWidth="1"
                    opacity="0.35"
                />
            </svg>

            {/* Information particles */}
            {[0, 1, 2, 3, 4].map((particle) => (
                <motion.div
                    key={particle}
                    className="
                        absolute
                        left-[7%]
                        top-1/2
                        h-1.5
                        w-1.5
                        rounded-full
                        bg-white
                        shadow-[0_0_14px_rgba(255,255,255,0.7)]
                    "
                    animate={{
                        left: ["7%", "28%", "50%", "72%", "92%"],
                        top: ["50%", "22%", "50%", "22%", "50%"],
                        opacity: [0, 1, 1, 1, 0],
                        scale: [0.6, 1, 1.1, 1, 0.6],
                    }}
                    transition={{
                        duration: 6,
                        repeat: Infinity,
                        delay: particle * 1.15,
                        ease: "easeInOut",
                    }}
                />
            ))}

            {/* Nodes */}
            {nodes.map((node, index) => {
                const tone = toneMap[node.tone];

                return (
                    <motion.div
                        key={node.id}
                        className="
                            absolute
                            -translate-x-1/2
                            -translate-y-1/2
                        "
                        style={{
                            left: node.x,
                            top: node.y,
                        }}
                        initial={{
                            opacity: 0,
                            scale: 0.8,
                        }}
                        animate={{
                            opacity: 1,
                            scale: [1, 1.025, 1],
                        }}
                        transition={{
                            opacity: {
                                duration: 0.7,
                                delay: index * 0.15,
                            },
                            scale: {
                                duration: 4,
                                repeat: Infinity,
                                ease: "easeInOut",
                                delay: index * 0.3,
                            },
                        }}
                    >
                        <div
                            className={`
                                group
                                relative
                                flex
                                min-w-[112px]
                                flex-col
                                items-center
                                rounded-[24px]
                                border
                                ${tone.border}
                                bg-white/[0.038]
                                px-4
                                py-4
                                backdrop-blur-[28px]
                                ${tone.glow}
                                transition-all
                                duration-500
                                hover:scale-105
                                hover:bg-white/[0.07]
                            `}
                        >

                            {/* Node indicator */}
                            <motion.div
                                animate={{
                                    opacity: [0.45, 1, 0.45],
                                }}
                                transition={{
                                    duration: 3,
                                    repeat: Infinity,
                                    delay: index * 0.4,
                                }}
                                className={`
                                    mb-3
                                    h-1.5
                                    w-1.5
                                    rounded-full
                                    ${tone.dot}
                                `}
                            />

                            <span className="
                                text-[11px]
                                font-medium
                                tracking-wide
                                text-white/85
                            ">
                                {node.label}
                            </span>

                            <span
                                className={`
                                    mt-1
                                    whitespace-nowrap
                                    text-[7px]
                                    uppercase
                                    tracking-[0.15em]
                                    ${tone.text}
                                    opacity-45
                                `}
                            >
                                {node.sub}
                            </span>

                            {/* Specular edge */}
                            <span
                                className="
                                    pointer-events-none
                                    absolute
                                    inset-x-4
                                    top-0
                                    h-px
                                    bg-gradient-to-r
                                    from-transparent
                                    via-white/35
                                    to-transparent
                                "
                            />

                            {/* Lower glass reflection */}
                            <span
                                className="
                                    pointer-events-none
                                    absolute
                                    inset-x-6
                                    bottom-1
                                    h-px
                                    bg-white/[0.035]
                                    blur-[1px]
                                "
                            />
                        </div>
                    </motion.div>
                );
            })}
        </div>
    );
}

export default HelixFlow;