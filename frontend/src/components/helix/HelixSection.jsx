import { motion } from "framer-motion";
import { ArrowDown, ArrowUpRight } from "lucide-react";

import HelixCore from "./HelixCore";
import GlassPill from "../ui/GlassPill";

function HelixSection() {
    return (
        <section
            id="helix"
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
            {/* Atmospheric light */}
            <motion.div
                animate={{
                    scale: [0.9, 1.08, 0.9],
                    opacity: [0.12, 0.22, 0.12],
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
                    top-[42%]
                    h-[700px]
                    w-[900px]
                    -translate-x-1/2
                    -translate-y-1/2
                    rounded-full
                    bg-gradient-to-r
                    from-violet-500/[0.06]
                    via-white/[0.015]
                    to-cyan-400/[0.06]
                    blur-[160px]
                "
            />

            <div className="relative z-10 mx-auto max-w-[1400px]">

                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.25 }}
                    transition={{
                        duration: 0.9,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="mx-auto max-w-4xl text-center"
                >
                    <GlassPill>
                        Helix Intelligence Engine
                    </GlassPill>

                    <h2
                        className="
                            mt-8
                            text-5xl
                            font-medium
                            leading-[0.92]
                            tracking-[-0.065em]
                            text-white
                            sm:text-6xl
                            lg:text-8xl
                        "
                    >
                        The intelligence
                        <br />
                        <span
                            className="
                                bg-gradient-to-r
                                from-violet-200
                                via-white
                                to-cyan-200
                                bg-clip-text
                                text-transparent
                            "
                        >
                            inside Cognexa.
                        </span>
                    </h2>

                    <p
                        className="
                            mx-auto
                            mt-7
                            max-w-2xl
                            text-sm
                            leading-7
                            text-white/35
                            sm:text-base
                        "
                    >
                        Helix transforms raw information into structured,
                        searchable, and context-aware knowledge through
                        adaptive processing and intelligent retrieval.
                    </p>
                </motion.div>

                {/* Helix Engine */}
                <motion.div
                    initial={{
                        opacity: 0,
                        y: 60,
                        scale: 0.96,
                    }}
                    whileInView={{
                        opacity: 1,
                        y: 0,
                        scale: 1,
                    }}
                    viewport={{
                        once: true,
                        amount: 0.15,
                    }}
                    transition={{
                        duration: 1.1,
                        delay: 0.15,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="mt-20"
                >
                    <HelixCore />
                </motion.div>

                {/* Architecture explanation */}
                <div className="mt-12 grid gap-4 lg:grid-cols-3">

                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.7 }}
                        className="
                            rounded-[26px]
                            border
                            border-white/[0.07]
                            bg-white/[0.018]
                            p-6
                            backdrop-blur-xl
                        "
                    >
                        <span className="text-[9px] uppercase tracking-[0.25em] text-violet-200/45">
                            01 / Structure
                        </span>

                        <h3 className="mt-4 text-lg font-medium text-white/85">
                            HAC
                        </h3>

                        <p className="mt-3 text-sm leading-6 text-white/30">
                            Information is intelligently structured while
                            preserving the relationships and context inside
                            the original document.
                        </p>
                    </motion.div>

                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{
                            duration: 0.7,
                            delay: 0.1,
                        }}
                        className="
                            rounded-[26px]
                            border
                            border-white/[0.07]
                            bg-white/[0.018]
                            p-6
                            backdrop-blur-xl
                        "
                    >
                        <span className="text-[9px] uppercase tracking-[0.25em] text-white/35">
                            02 / Representation
                        </span>

                        <h3 className="mt-4 text-lg font-medium text-white/85">
                            Semantic Layer
                        </h3>

                        <p className="mt-3 text-sm leading-6 text-white/30">
                            Structured information becomes machine-readable
                            semantic representations that capture meaning,
                            rather than simple text similarity.
                        </p>
                    </motion.div>

                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{
                            duration: 0.7,
                            delay: 0.2,
                        }}
                        className="
                            rounded-[26px]
                            border
                            border-white/[0.07]
                            bg-white/[0.018]
                            p-6
                            backdrop-blur-xl
                        "
                    >
                        <span className="text-[9px] uppercase tracking-[0.25em] text-cyan-200/45">
                            03 / Retrieval
                        </span>

                        <h3 className="mt-4 text-lg font-medium text-white/85">
                            HARE
                        </h3>

                        <p className="mt-3 text-sm leading-6 text-white/30">
                            Relevant context is dynamically retrieved so
                            downstream intelligence can reason over the
                            information that actually matters.
                        </p>
                    </motion.div>

                </div>

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
                        gap-4
                        text-center
                    "
                >
                    <div className="flex items-center gap-3">
                        <span className="h-px w-12 bg-white/[0.08]" />

                        <span
                            className="
                                text-[9px]
                                uppercase
                                tracking-[0.3em]
                                text-white/20
                            "
                        >
                            From information to intelligence
                        </span>

                        <span className="h-px w-12 bg-white/[0.08]" />
                    </div>

                    <ArrowDown
                        size={14}
                        className="text-cyan-200/35"
                    />
                </motion.div>

            </div>
        </section>
    );
}

export default HelixSection;
