import { motion } from "framer-motion";
import { Sparkles, ArrowUpRight } from "lucide-react";
import { useNavigate } from "react-router-dom";

function Navbar() {
    const navigate = useNavigate();

    const navigation = [
        { label: "What We Do", target: "what-we-do" },
        { label: "Helix", target: "helix" },
        { label: "Who We Are", target: "who-we-are" },
    ];

    const scrollToSection = (id) => {
        const section = document.getElementById(id);

        if (section) {
            section.scrollIntoView({
                behavior: "smooth",
                block: "start",
            });
        }
    };

    return (
        <motion.header
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="
                fixed
                left-1/2
                top-5
                z-50
                w-[calc(100%-32px)]
                max-w-[1120px]
                -translate-x-1/2
            "
        >
            <nav
                className="
                    relative
                    flex
                    h-14
                    items-center
                    justify-between
                    rounded-full
                    border
                    border-white/[0.12]
                    bg-white/[0.045]
                    px-3
                    shadow-[inset_0_1px_1px_rgba(255,255,255,0.13),0_15px_60px_rgba(0,0,0,0.22)]
                    backdrop-blur-[30px]
                "
            >
                {/* Reflection */}
                <span
                    className="
                        pointer-events-none
                        absolute
                        inset-x-[15%]
                        top-0
                        h-px
                        bg-gradient-to-r
                        from-transparent
                        via-white/30
                        to-transparent
                    "
                />

                {/* Logo */}
                <button
                    type="button"
                    onClick={() => navigate("/")}
                    className="relative flex items-center gap-2.5"
                >
                    <div
                        className="
                            flex
                            h-9
                            w-9
                            items-center
                            justify-center
                            rounded-full
                            border
                            border-white/[0.12]
                            bg-white/[0.08]
                            text-violet-200
                            shadow-[inset_0_1px_1px_rgba(255,255,255,0.15)]
                        "
                    >
                        <Sparkles size={15} />
                    </div>

                    <span className="text-[11px] font-semibold tracking-[0.22em] text-white/85">
                        COGNEXA
                    </span>
                </button>

                {/* Navigation */}
                <div
                    className="
                        absolute
                        left-1/2
                        hidden
                        -translate-x-1/2
                        items-center
                        gap-1
                        rounded-full
                        border
                        border-white/[0.07]
                        bg-black/[0.12]
                        p-1
                        backdrop-blur-xl
                        md:flex
                    "
                >
                    {navigation.map((item) => (
                        <button
                            key={item.target}
                            type="button"
                            onClick={() => scrollToSection(item.target)}
                            className="
                                rounded-full
                                px-4
                                py-2
                                text-[10px]
                                font-medium
                                text-white/55
                                transition-all
                                hover:bg-white/[0.08]
                                hover:text-white
                            "
                        >
                            {item.label}
                        </button>
                    ))}
                </div>

                {/* Enter Cognexa */}
                <button
                    type="button"
                    onClick={() => navigate("/signup")}
                    className="
                        group
                        flex
                        items-center
                        gap-2
                        rounded-full
                        border
                        border-white/[0.12]
                        bg-white/[0.08]
                        px-4
                        py-2.5
                        text-[10px]
                        font-medium
                        text-white/80
                        backdrop-blur-xl
                        transition-all
                        hover:bg-white/[0.14]
                    "
                >
                    Enter Cognexa

                    <ArrowUpRight
                        size={13}
                        className="
                            transition-transform
                            group-hover:-translate-y-0.5
                            group-hover:translate-x-0.5
                        "
                    />
                </button>
            </nav>
        </motion.header>
    );
}

export default Navbar;

