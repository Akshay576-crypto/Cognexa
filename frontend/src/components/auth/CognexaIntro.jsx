import { motion, AnimatePresence } from "framer-motion";
import { useEffect, useState } from "react";

function CognexaIntro({ onComplete }) {
    const [phase, setPhase] = useState("enter");

    useEffect(() => {
        const revealTimer = setTimeout(() => {
            setPhase("reveal");
        }, 1150);

        const completeTimer = setTimeout(() => {
            onComplete();
        }, 1750);

        return () => {
            clearTimeout(revealTimer);
            clearTimeout(completeTimer);
        };
    }, [onComplete]);

    const skipIntro = () => {
        onComplete();
    };

    return (
        <AnimatePresence>
            <motion.div
                key="cognexa-intro"
                onClick={skipIntro}
                initial={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                transition={{ duration: 0.35 }}
                className="
                    fixed
                    inset-0
                    z-[100]
                    flex
                    cursor-pointer
                    items-center
                    justify-center
                    overflow-hidden
                    bg-[#08090c]
                "
            >
                {/* Central intelligence glow */}
                <motion.div
                    initial={{
                        scale: 0.5,
                        opacity: 0,
                    }}
                    animate={{
                        scale: [0.7, 1, 1.4],
                        opacity: [0, 0.12, 0],
                    }}
                    transition={{
                        duration: 1.6,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="
                        pointer-events-none
                        absolute
                        h-[500px]
                        w-[500px]
                        rounded-full
                        bg-violet-400
                        blur-[140px]
                    "
                />

                {/* Cyan secondary glow */}
                <motion.div
                    initial={{
                        scale: 0.6,
                        opacity: 0,
                    }}
                    animate={{
                        scale: [0.8, 1.1, 1.5],
                        opacity: [0, 0.08, 0],
                    }}
                    transition={{
                        duration: 1.8,
                        delay: 0.1,
                        ease: "easeOut",
                    }}
                    className="
                        pointer-events-none
                        absolute
                        h-[300px]
                        w-[300px]
                        rounded-full
                        bg-cyan-300
                        blur-[120px]
                    "
                />

                {/* Cognexa C */}
                <motion.div
                    initial={{
                        scale: 0.12,
                        opacity: 0,
                        rotate: -8,
                    }}
                    animate={{
                        scale:
                            phase === "reveal"
                                ? 18
                                : [0.12, 0.55, 1],
                        opacity:
                            phase === "reveal"
                                ? 0
                                : [0, 1, 1],
                        rotate:
                            phase === "reveal"
                                ? 0
                                : [-8, 0, 0],
                    }}
                    transition={{
                        duration:
                            phase === "reveal"
                                ? 0.55
                                : 0.9,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="
                        relative
                        z-10
                        flex
                        h-28
                        w-28
                        items-center
                        justify-center
                        rounded-full
                        border
                        border-white/[0.16]
                        bg-white/[0.035]
                        shadow-[0_0_80px_rgba(167,139,250,0.12)]
                    "
                >
                    {/* Inner ring */}
                    <span
                        className="
                            absolute
                            inset-3
                            rounded-full
                            border
                            border-violet-200/[0.12]
                        "
                    />

                    {/* C */}
                    <span
                        className="
                            relative
                            z-10
                            text-7xl
                            font-medium
                            tracking-[-0.12em]
                            text-white
                        "
                    >
                        C
                    </span>
                </motion.div>

                {/* Cognexa wordmark */}
                <motion.div
                    initial={{
                        opacity: 0,
                        y: 12,
                    }}
                    animate={{
                        opacity:
                            phase === "reveal"
                                ? 1
                                : 0,
                        y:
                            phase === "reveal"
                                ? 0
                                : 12,
                    }}
                    transition={{
                        duration: 0.45,
                        delay: 0.05,
                    }}
                    className="
                        absolute
                        bottom-[28%]
                        z-20
                        text-center
                    "
                >
                    <p
                        className="
                            text-[10px]
                            uppercase
                            tracking-[0.45em]
                            text-white/45
                        "
                    >
                        Cognexa Intelligence
                    </p>
                </motion.div>

                {/* Development hint */}
                <motion.p
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.5 }}
                    className="
                        absolute
                        bottom-8
                        z-20
                        text-[8px]
                        uppercase
                        tracking-[0.3em]
                        text-white/15
                    "
                >
                    Click to skip
                </motion.p>
            </motion.div>
        </AnimatePresence>
    );
}

export default CognexaIntro;
