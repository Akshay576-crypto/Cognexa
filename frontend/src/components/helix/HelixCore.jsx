import { motion } from "framer-motion";
import HelixFlow from "./HelixFlow";
import GlassPill from "../ui/GlassPill";

function HelixCore() {
    return (
        <div className="relative w-full">

            {/* Soft intelligence illumination */}
            <motion.div
                animate={{
                    scale: [0.92, 1.08, 0.92],
                    opacity: [0.08, 0.16, 0.08],
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
                    top-1/2
                    h-[440px]
                    w-[760px]
                    -translate-x-1/2
                    -translate-y-1/2
                    rounded-full
                    bg-white/[0.035]
                    blur-[110px]
                "
            />

            {/* Main liquid glass surface */}
            <div
                className="
                    relative
                    overflow-hidden
                    rounded-[40px]
                    border
                    border-white/[0.105]
                    bg-white/[0.035]
                    px-6
                    py-7
                    shadow-[
                        inset_0_1px_0_rgba(255,255,255,0.16),
                        inset_0_-1px_0_rgba(255,255,255,0.025),
                        0_35px_120px_rgba(0,0,0,0.30)
                    ]
                    backdrop-blur-[35px]
                "
            >

                {/* Glass reflection */}
                <div
                    className="
                        pointer-events-none
                        absolute
                        inset-x-[10%]
                        top-0
                        h-px
                        bg-gradient-to-r
                        from-transparent
                        via-white/40
                        to-transparent
                    "
                />

                {/* Soft internal reflection */}
                <div
                    className="
                        pointer-events-none
                        absolute
                        left-[-10%]
                        top-[-50%]
                        h-[250px]
                        w-[70%]
                        rotate-[-8deg]
                        rounded-full
                        bg-white/[0.025]
                        blur-[60px]
                    "
                />

                {/* Header */}
                <div className="relative z-10 flex items-center justify-between">

                    <div>
                        <p className="
                            text-[8px]
                            uppercase
                            tracking-[0.32em]
                            text-white/30
                        ">
                            Cognexa
                        </p>

                        <h2 className="
                            mt-1
                            text-sm
                            font-medium
                            tracking-tight
                            text-white/85
                        ">
                            Helix Intelligence Engine
                        </h2>
                    </div>

                    <GlassPill>
                        Live system
                    </GlassPill>
                </div>

                {/* Intelligence flow */}
                <div className="relative z-10 mt-5 overflow-x-auto overflow-y-hidden">
                    <HelixFlow />
                </div>

                {/* System status */}
                <div className="
                    relative
                    z-10
                    flex
                    items-center
                    justify-between
                    border-t
                    border-white/[0.065]
                    pt-4
                ">

                    <div className="flex items-center gap-2">

                        <motion.span
                            animate={{
                                opacity: [0.35, 1, 0.35],
                                scale: [0.9, 1.15, 0.9],
                            }}
                            transition={{
                                duration: 2.5,
                                repeat: Infinity,
                            }}
                            className="
                                h-1.5
                                w-1.5
                                rounded-full
                                bg-[#d9dce3]
                                shadow-[0_0_12px_rgba(255,255,255,0.45)]
                            "
                        />

                        <span className="
                            text-[8px]
                            uppercase
                            tracking-[0.2em]
                            text-white/35
                        ">
                            Information flow active
                        </span>
                    </div>

                    <span className="
                        text-[8px]
                        uppercase
                        tracking-[0.2em]
                        text-white/20
                    ">
                        HAC → Embeddings → HARE
                    </span>
                </div>
            </div>
        </div>
    );
}

export default HelixCore;