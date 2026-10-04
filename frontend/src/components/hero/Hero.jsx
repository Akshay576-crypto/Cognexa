import { motion } from "framer-motion";
import { ArrowDown, Sparkles } from "lucide-react";

import HeroBackground from "./HeroBackground";
import HelixCore from "../helix/HelixCore";
import GlassButton from "../ui/GlassButton";
import GlassPill from "../ui/GlassPill";

function Hero() {
    return (
        <section
            className="
                relative
                min-h-screen
                overflow-hidden
                bg-[#08090c]
                pt-28
            "
        >
            <HeroBackground />

            <div className="
                relative
                z-10
                mx-auto
                max-w-[1450px]
                px-6
                lg:px-10
            ">

                {/* Eyebrow */}
                <div className="flex flex-col items-center text-center">

                    <motion.div
                        initial={{
                            opacity: 0,
                            y: 15,
                        }}
                        animate={{
                            opacity: 1,
                            y: 0,
                        }}
                        transition={{
                            duration: 0.7,
                        }}
                    >
                        <GlassPill>
                            <Sparkles size={11} />
                            Intelligence reimagined
                        </GlassPill>
                    </motion.div>

                    {/* Main statement */}
                    <motion.h1
                        initial={{
                            opacity: 0,
                            y: 30,
                        }}
                        animate={{
                            opacity: 1,
                            y: 0,
                        }}
                        transition={{
                            duration: 1,
                            delay: 0.15,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                        className="
                            mt-8
                            max-w-[1050px]
                            text-6xl
                            font-medium
                            leading-[0.9]
                            tracking-[-0.07em]
                            text-white
                            sm:text-7xl
                            lg:text-[100px]
                            xl:text-[120px]
                        "
                    >
                        Information

                        <span className="text-white/25">
                            {" "}becomes{" "}
                        </span>

                        <span
                            className="
                                bg-gradient-to-b
                                from-white
                                via-[#e4e5ea]
                                to-[#aaaeb8]
                                bg-clip-text
                                text-transparent
                            "
                        >
                            intelligence.
                        </span>
                    </motion.h1>

                    {/* Description */}
                    <motion.p
                        initial={{
                            opacity: 0,
                            y: 20,
                        }}
                        animate={{
                            opacity: 1,
                            y: 0,
                        }}
                        transition={{
                            duration: 0.8,
                            delay: 0.35,
                        }}
                        className="
                            mt-7
                            max-w-xl
                            text-sm
                            leading-6
                            text-white/38
                            sm:text-base
                        "
                    >
                        Cognexa transforms fragmented information into
                        structured knowledge, semantic representations,
                        and intelligent retrieval.
                    </motion.p>

                    {/* Actions */}
                    <motion.div
                        initial={{
                            opacity: 0,
                            y: 15,
                        }}
                        animate={{
                            opacity: 1,
                            y: 0,
                        }}
                        transition={{
                            duration: 0.8,
                            delay: 0.5,
                        }}
                        className="mt-8 flex gap-3"
                    >
                        <GlassButton variant="bright">
                            Explore Cognexa
                        </GlassButton>

                        <GlassButton>
                            Enter Helix
                        </GlassButton>
                    </motion.div>
                </div>

                {/* Helix */}
                <motion.div
                    initial={{
                        opacity: 0,
                        y: 60,
                        scale: 0.96,
                    }}
                    animate={{
                        opacity: 1,
                        y: 0,
                        scale: 1,
                    }}
                    transition={{
                        duration: 1.2,
                        delay: 0.45,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="
                        mx-auto
                        mt-20
                        max-w-[1180px]
                    "
                >
                    <HelixCore />
                </motion.div>

                {/* Scroll indicator */}
                <motion.div
                    animate={{
                        y: [0, 6, 0],
                    }}
                    transition={{
                        duration: 2,
                        repeat: Infinity,
                        ease: "easeInOut",
                    }}
                    className="
                        mx-auto
                        mt-8
                        flex
                        w-fit
                        items-center
                        gap-2
                        pb-10
                        text-[8px]
                        uppercase
                        tracking-[0.3em]
                        text-white/22
                    "
                >
                    Explore the intelligence layer

                    <ArrowDown size={12} />
                </motion.div>

            </div>
        </section>
    );
}

export default Hero;