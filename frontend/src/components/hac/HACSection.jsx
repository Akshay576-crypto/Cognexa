import { motion } from "framer-motion";
import { ArrowDown } from "lucide-react";

import HACDocument from "./HACDocument";
import HACFlow from "./HACFlow";

function HACSection() {
    return (
        <section
            id="hac"
            className="
                relative
                overflow-hidden
                bg-[#08090c]
                px-6
                py-32
                lg:px-10
                lg:py-44
            "
        >
            {/* Ambient intelligence light */}
            <motion.div
                animate={{
                    scale: [1, 1.12, 1],
                    opacity: [0.08, 0.14, 0.08],
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
                    top-[35%]
                    h-[700px]
                    w-[700px]
                    -translate-x-1/2
                    -translate-y-1/2
                    rounded-full
                    bg-violet-500/[0.06]
                    blur-[160px]
                "
            />

            {/* Subtle cyan atmosphere */}
            <div
                className="
                    pointer-events-none
                    absolute
                    right-[-15%]
                    top-[45%]
                    h-[500px]
                    w-[500px]
                    rounded-full
                    bg-cyan-400/[0.025]
                    blur-[150px]
                "
            />

            <div className="relative z-10 mx-auto max-w-[1250px]">

                {/* Section introduction */}
                <motion.div
                    initial={{ opacity: 0, y: 25 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.3 }}
                    transition={{
                        duration: 0.8,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="max-w-3xl"
                >
                    <div className="flex items-center gap-3">
                        <span className="h-px w-8 bg-violet-300/30" />

                        <span className="
                            text-[9px]
                            font-medium
                            uppercase
                            tracking-[0.32em]
                            text-violet-200/55
                        ">
                            01 / HAC
                        </span>
                    </div>

                    <h2
                        className="
                            mt-6
                            text-4xl
                            font-medium
                            leading-[1.02]
                            tracking-[-0.05em]
                            text-white
                            sm:text-5xl
                            lg:text-7xl
                        "
                    >
                        Structure before
                        <br />

                        <span className="text-white/30">
                            segmentation.
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
                        Helix Adaptive Chunking understands the structure of
                        information before dividing it. Instead of blindly
                        splitting text, Cognexa preserves the relationships
                        that give every piece of information its meaning.
                    </p>
                </motion.div>

                {/* Main visual */}
                <div className="mt-20 grid items-center gap-12 lg:grid-cols-[0.9fr_1.1fr] lg:gap-20">

                    {/* Document */}
                    <div>
                        <HACDocument />
                    </div>

                    {/* Flow */}
                    <div>
                        <HACFlow />
                    </div>

                </div>

                {/* Philosophy */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{
                        duration: 0.8,
                        delay: 0.2,
                    }}
                    className="
                        mx-auto
                        mt-24
                        max-w-2xl
                        text-center
                    "
                >
                    <p
                        className="
                            text-[9px]
                            uppercase
                            tracking-[0.32em]
                            text-white/20
                        "
                    >
                        The HAC principle
                    </p>

                    <p
                        className="
                            mt-5
                            text-lg
                            font-light
                            leading-8
                            tracking-[-0.01em]
                            text-white/55
                            sm:text-xl
                        "
                    >
                        Information should not lose its meaning
                        <span className="text-white/20"> just because it became a chunk.</span>
                    </p>
                </motion.div>

                {/* Transition */}
                <motion.div
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{
                        duration: 1,
                        delay: 0.3,
                    }}
                    className="
                        mt-24
                        flex
                        flex-col
                        items-center
                        gap-3
                    "
                >
                    <span
                        className="
                            text-[8px]
                            uppercase
                            tracking-[0.3em]
                            text-white/15
                        "
                    >
                        From structure to meaning
                    </span>

                    <ArrowDown
                        size={14}
                        className="text-violet-200/30"
                    />
                </motion.div>

            </div>
        </section>
    );
}

export default HACSection;