import { motion } from "framer-motion";
import { ArrowDown, Network, Search, Sparkles } from "lucide-react";

const capabilities = [
    {
        number: "01",
        title: "Understand",
        label: "INFORMATION",
        description:
            "Cognexa transforms fragmented information into structured context that systems and people can understand.",
        icon: Network,
        accent: "violet",
    },
    {
        number: "02",
        title: "Connect",
        label: "SEMANTIC SPACE",
        description:
            "Information is represented semantically so relationships between knowledge can be discovered.",
        icon: Sparkles,
        accent: "white",
    },
    {
        number: "03",
        title: "Retrieve",
        label: "INTELLIGENCE",
        description:
            "Helix intelligently searches the right context instead of treating every document as a flat collection of text.",
        icon: Search,
        accent: "cyan",
    },
];

const accents = {
    violet: {
        glow: "bg-violet-400/[0.07]",
        border: "border-violet-300/[0.14]",
        icon: "text-violet-200",
    },
    white: {
        glow: "bg-white/[0.045]",
        border: "border-white/[0.12]",
        icon: "text-white",
    },
    cyan: {
        glow: "bg-cyan-300/[0.06]",
        border: "border-cyan-300/[0.14]",
        icon: "text-cyan-200",
    },
};

function WhatWeDo() {
    return (
        <section
            id="what-we-do"
            className="
                relative
                overflow-hidden
                bg-[#08090c]
                px-6
                py-32
                sm:px-10
                lg:px-16
                lg:py-40
            "
        >
            {/* Cognexa atmosphere */}
            <motion.div
                animate={{
                    x: ["-8%", "8%", "-8%"],
                    y: ["-5%", "6%", "-5%"],
                    scale: [1, 1.12, 1],
                }}
                transition={{
                    duration: 18,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="
                    pointer-events-none
                    absolute
                    left-[-10%]
                    top-[20%]
                    h-[420px]
                    w-[420px]
                    rounded-full
                    bg-violet-500/[0.055]
                    blur-[150px]
                "
            />

            <motion.div
                animate={{
                    x: ["8%", "-8%", "8%"],
                    y: ["5%", "-5%", "5%"],
                    scale: [1.1, 0.9, 1.1],
                }}
                transition={{
                    duration: 21,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="
                    pointer-events-none
                    absolute
                    right-[-10%]
                    bottom-[10%]
                    h-[400px]
                    w-[400px]
                    rounded-full
                    bg-cyan-400/[0.045]
                    blur-[150px]
                "
            />

            <div className="relative z-10 mx-auto max-w-[1250px]">

                {/* Heading */}
                <motion.div
                    initial={{ opacity: 0, y: 25 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.3 }}
                    transition={{ duration: 0.8 }}
                    className="max-w-3xl"
                >
                    <div
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
                            text-white/40
                            backdrop-blur-xl
                        "
                    >
                        <span className="h-1.5 w-1.5 rounded-full bg-cyan-200/80 shadow-[0_0_12px_rgba(165,243,252,0.7)]" />
                        Cognexa intelligence layer
                    </div>

                    <h2
                        className="
                            mt-7
                            text-4xl
                            font-medium
                            leading-[0.98]
                            tracking-[-0.055em]
                            text-white
                            sm:text-5xl
                            lg:text-6xl
                        "
                    >
                        Intelligence begins
                        <br />
                        <span className="text-white/30">
                            with understanding.
                        </span>
                    </h2>

                    <p
                        className="
                            mt-7
                            max-w-2xl
                            text-sm
                            leading-7
                            text-white/35
                            sm:text-base
                        "
                    >
                        Cognexa transforms complex information into
                        structured knowledge, semantic context, and
                        intelligent retrieval.
                    </p>
                </motion.div>

                {/* Capability system */}
                <div className="relative mt-20">

                    {/* Information stream */}
                    <div
                        className="
                            pointer-events-none
                            absolute
                            left-[12%]
                            right-[12%]
                            top-1/2
                            hidden
                            h-px
                            -translate-y-1/2
                            lg:block
                        "
                    >
                        <div className="absolute inset-0 bg-gradient-to-r from-violet-300/0 via-white/15 to-cyan-300/0" />

                        <motion.div
                            animate={{
                                left: ["0%", "100%"],
                                opacity: [0, 1, 1, 0],
                            }}
                            transition={{
                                duration: 5,
                                repeat: Infinity,
                                ease: "linear",
                            }}
                            className="
                                absolute
                                top-1/2
                                h-1.5
                                w-1.5
                                -translate-y-1/2
                                rounded-full
                                bg-white
                                shadow-[0_0_16px_rgba(255,255,255,0.9)]
                            "
                        />
                    </div>

                    <div className="grid gap-5 md:grid-cols-3">
                        {capabilities.map((item, index) => {
                            const style = accents[item.accent];
                            const Icon = item.icon;

                            return (
                                <motion.div
                                    key={item.number}
                                    initial={{
                                        opacity: 0,
                                        y: 30,
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
                                        delay: index * 0.14,
                                    }}
                                    className="relative"
                                >
                                    <div
                                        className={`
                                            group
                                            relative
                                            min-h-[310px]
                                            overflow-hidden
                                            rounded-[32px]
                                            border
                                            ${style.border}
                                            ${style.glow}
                                            p-7
                                            backdrop-blur-[35px]
                                            transition-all
                                            duration-500
                                            hover:-translate-y-2
                                            hover:bg-white/[0.055]
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

                                        {/* Ambient card light */}
                                        <div
                                            className={`
                                                pointer-events-none
                                                absolute
                                                -right-20
                                                -top-20
                                                h-48
                                                w-48
                                                rounded-full
                                                ${style.glow}
                                                blur-[70px]
                                                transition-transform
                                                duration-700
                                                group-hover:scale-150
                                            `}
                                        />

                                        {/* Top */}
                                        <div className="relative z-10 flex items-center justify-between">
                                            <span className="text-[9px] tracking-[0.25em] text-white/20">
                                                {item.number}
                                            </span>

                                            <Icon
                                                size={17}
                                                strokeWidth={1.4}
                                                className={style.icon}
                                            />
                                        </div>

                                        {/* Content */}
                                        <div className="relative z-10 mt-12">
                                            <div className="flex items-center gap-3">
                                                <span
                                                    className={`
                                                        h-1.5
                                                        w-1.5
                                                        rounded-full
                                                        ${style.icon.replace(
                                                        "text-",
                                                        "bg-",
                                                    )}
                                                    `}
                                                />

                                                <span className="text-[9px] uppercase tracking-[0.25em] text-white/35">
                                                    {item.label}
                                                </span>
                                            </div>

                                            <h3 className="mt-5 text-2xl font-medium tracking-[-0.04em] text-white/90">
                                                {item.title}
                                            </h3>

                                            <p className="mt-4 text-sm leading-6 text-white/35">
                                                {item.description}
                                            </p>
                                        </div>

                                        {/* Bottom system line */}
                                        <div className="absolute bottom-6 left-7 right-7 flex items-center justify-between">
                                            <span className="text-[8px] uppercase tracking-[0.2em] text-white/15">
                                                Cognexa system
                                            </span>

                                            <span className="h-px w-12 bg-gradient-to-r from-transparent via-white/20 to-transparent" />
                                        </div>
                                    </div>
                                </motion.div>
                            );
                        })}
                    </div>
                </div>

                {/* Transition */}
                <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8 }}
                    className="
                        mt-16
                        flex
                        flex-col
                        items-center
                        gap-3
                    "
                >
                    <span className="text-[9px] uppercase tracking-[0.32em] text-white/20">
                        Information → Meaning → Intelligence
                    </span>

                    <motion.div
                        animate={{ y: [0, 5, 0] }}
                        transition={{
                            duration: 2,
                            repeat: Infinity,
                            ease: "easeInOut",
                        }}
                    >
                        <ArrowDown
                            size={14}
                            strokeWidth={1}
                            className="text-white/25"
                        />
                    </motion.div>
                </motion.div>
            </div>
        </section>
    );
}

export default WhatWeDo;