import { motion } from "framer-motion";
import { ArrowDown } from "lucide-react";

function WhoWeAre() {
    return (
        <section
            id="who-we-are"
            className="
                relative
                min-h-screen
                overflow-hidden
                bg-[#08090c]
                px-6
                py-32
                lg:px-10
                lg:py-44
            "
        >
            {/* Ambient atmosphere */}
            <div
                className="
                    pointer-events-none
                    absolute
                    left-[20%]
                    top-[25%]
                    h-[500px]
                    w-[500px]
                    rounded-full
                    bg-violet-400/[0.025]
                    blur-[150px]
                "
            />

            <div
                className="
                    pointer-events-none
                    absolute
                    right-[15%]
                    bottom-[20%]
                    h-[450px]
                    w-[450px]
                    rounded-full
                    bg-cyan-400/[0.02]
                    blur-[150px]
                "
            />

            <div className="relative z-10 mx-auto max-w-[1250px]">

                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: 25 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.3 }}
                    transition={{
                        duration: 0.8,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="max-w-4xl"
                >
                    <p
                        className="
                            mb-5
                            text-[10px]
                            font-medium
                            uppercase
                            tracking-[0.3em]
                            text-violet-300/60
                        "
                    >
                        Who We Are
                    </p>

                    <h2
                        className="
                            text-4xl
                            font-medium
                            leading-[1.02]
                            tracking-[-0.055em]
                            text-white
                            sm:text-5xl
                            lg:text-7xl
                        "
                    >
                        We build systems
                        <br />
                        that <span className="text-white/30">understand.</span>
                    </h2>

                    <p
                        className="
                            mt-8
                            max-w-2xl
                            text-sm
                            leading-7
                            text-white/40
                            sm:text-base
                        "
                    >
                        Cognexa is an intelligence platform built around a
                        simple idea: information becomes powerful when systems
                        can understand its structure, meaning, and relationships.
                    </p>
                </motion.div>

                {/* Identity panel */}
                <motion.div
                    initial={{ opacity: 0, y: 35 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.2 }}
                    transition={{
                        duration: 0.9,
                        delay: 0.15,
                    }}
                    className="
                        relative
                        mt-20
                        overflow-hidden
                        rounded-[38px]
                        border
                        border-white/[0.08]
                        bg-white/[0.018]
                        p-7
                        backdrop-blur-xl
                        sm:p-10
                        lg:p-14
                    "
                >
                    {/* Reflection */}
                    <div
                        className="
                            pointer-events-none
                            absolute
                            inset-x-[10%]
                            top-0
                            h-px
                            bg-gradient-to-r
                            from-transparent
                            via-white/25
                            to-transparent
                        "
                    />

                    <div className="grid gap-14 lg:grid-cols-[0.8fr_1.2fr] lg:items-center">

                        {/* Cognexa mark */}
                        <div className="flex flex-col items-center justify-center lg:items-start">

                            <motion.div
                                animate={{
                                    scale: [1, 1.025, 1],
                                }}
                                transition={{
                                    duration: 5,
                                    repeat: Infinity,
                                    ease: "easeInOut",
                                }}
                                className="
                                    relative
                                    flex
                                    h-36
                                    w-36
                                    items-center
                                    justify-center
                                    rounded-full
                                    border
                                    border-white/[0.12]
                                    bg-white/[0.025]
                                    shadow-[0_0_80px_rgba(167,139,250,0.06)]
                                "
                            >
                                <div
                                    className="
                                        absolute
                                        inset-4
                                        rounded-full
                                        border
                                        border-violet-300/[0.12]
                                    "
                                />

                                <span
                                    className="
                                        text-6xl
                                        font-medium
                                        tracking-[-0.08em]
                                        text-white/90
                                    "
                                >
                                    C
                                </span>

                                <span
                                    className="
                                        absolute
                                        bottom-5
                                        text-[7px]
                                        uppercase
                                        tracking-[0.35em]
                                        text-violet-200/40
                                    "
                                >
                                    Cognexa
                                </span>
                            </motion.div>

                            <p
                                className="
                                    mt-6
                                    text-[8px]
                                    uppercase
                                    tracking-[0.3em]
                                    text-white/20
                                "
                            >
                                Intelligence infrastructure
                            </p>
                        </div>

                        {/* Philosophy */}
                        <div>
                            <p
                                className="
                                    text-[9px]
                                    uppercase
                                    tracking-[0.25em]
                                    text-white/20
                                "
                            >
                                Our perspective
                            </p>

                            <h3
                                className="
                                    mt-4
                                    max-w-xl
                                    text-2xl
                                    font-medium
                                    leading-tight
                                    tracking-[-0.035em]
                                    text-white/85
                                    sm:text-3xl
                                "
                            >
                                Intelligence is not about having
                                more information.
                                <span className="text-white/30">
                                    {" "}
                                    It is about understanding what matters.
                                </span>
                            </h3>

                            <p
                                className="
                                    mt-6
                                    max-w-xl
                                    text-sm
                                    leading-7
                                    text-white/35
                                "
                            >
                                Cognexa brings together structured knowledge,
                                semantic representations, adaptive retrieval,
                                and intelligent reasoning into one connected
                                intelligence layer.
                            </p>

                            <div
                                className="
                                    mt-8
                                    grid
                                    gap-4
                                    sm:grid-cols-3
                                "
                            >
                                <div>
                                    <p className="text-[9px] uppercase tracking-[0.2em] text-violet-200/50">
                                        Structure
                                    </p>
                                    <p className="mt-2 text-xs text-white/35">
                                        HAC
                                    </p>
                                </div>

                                <div>
                                    <p className="text-[9px] uppercase tracking-[0.2em] text-white/40">
                                        Meaning
                                    </p>
                                    <p className="mt-2 text-xs text-white/35">
                                        Embeddings
                                    </p>
                                </div>

                                <div>
                                    <p className="text-[9px] uppercase tracking-[0.2em] text-cyan-200/50">
                                        Retrieval
                                    </p>
                                    <p className="mt-2 text-xs text-white/35">
                                        HARE
                                    </p>
                                </div>
                            </div>
                        </div>

                    </div>
                </motion.div>

                {/* Closing statement */}
                <motion.div
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 1 }}
                    className="
                        mt-20
                        flex
                        flex-col
                        items-center
                        gap-3
                        text-center
                    "
                >
                    <span
                        className="
                            text-[9px]
                            uppercase
                            tracking-[0.3em]
                            text-white/15
                        "
                    >
                        Intelligence starts with context
                    </span>

                    <ArrowDown
                        size={14}
                        className="text-violet-300/40"
                    />
                </motion.div>

            </div>
        </section>
    );
}

export default WhoWeAre;