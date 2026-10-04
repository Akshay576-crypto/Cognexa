import { motion } from "framer-motion";
import { ArrowLeft, ArrowRight } from "lucide-react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { loginUser } from "../../api/auth";

function Login() {
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleLogin = async (event) => {
        event.preventDefault();

        setError("");

        if (!email.trim() || !password) {
            setError("Please enter your email and password.");
            return;
        }

        try {
            setLoading(true);

            await loginUser({
                email: email.trim(),
                password,
            });

            navigate("/chat");
        } catch (err) {
            setError(
                err.message || "Unable to sign in. Please try again."
            );
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="relative min-h-screen overflow-hidden bg-[#08090c] text-white">

            {/* Ambient atmosphere */}
            <motion.div
                animate={{
                    scale: [0.95, 1.05, 0.95],
                    opacity: [0.08, 0.16, 0.08],
                }}
                transition={{
                    duration: 9,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="
                    pointer-events-none
                    absolute
                    left-1/2
                    top-1/2
                    h-[650px]
                    w-[650px]
                    -translate-x-1/2
                    -translate-y-1/2
                    rounded-full
                    bg-violet-500/[0.06]
                    blur-[160px]
                "
            />

            <div
                className="
                    pointer-events-none
                    absolute
                    right-[10%]
                    top-[15%]
                    h-[300px]
                    w-[300px]
                    rounded-full
                    bg-cyan-400/[0.025]
                    blur-[130px]
                "
            />

            {/* Back */}
            <button
                type="button"
                onClick={() => navigate("/")}
                className="
                    absolute
                    left-6
                    top-6
                    z-20
                    flex
                    items-center
                    gap-2
                    text-[10px]
                    uppercase
                    tracking-[0.2em]
                    text-white/30
                    transition
                    hover:text-white/70
                "
            >
                <ArrowLeft size={13} />
                Cognexa
            </button>

            <div className="relative z-10 flex min-h-screen items-center justify-center px-6 py-20">

                <motion.div
                    initial={{ opacity: 0, y: 25, scale: 0.98 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    transition={{
                        duration: 0.8,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="w-full max-w-[430px]"
                >

                    {/* Cognexa C */}
                    <div className="mb-8 flex justify-center">
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
                                flex
                                h-16
                                w-16
                                items-center
                                justify-center
                                rounded-full
                                border
                                border-white/[0.12]
                                bg-white/[0.04]
                                shadow-[0_0_60px_rgba(167,139,250,0.06)]
                            "
                        >
                            <span className="text-3xl font-medium tracking-[-0.08em] text-white/90">
                                C
                            </span>
                        </motion.div>
                    </div>

                    {/* Heading */}
                    <div className="mb-8 text-center">
                        <p className="text-[9px] uppercase tracking-[0.3em] text-cyan-200/45">
                            Cognexa Intelligence
                        </p>

                        <h1 className="mt-3 text-3xl font-medium tracking-[-0.04em] text-white">
                            Welcome back
                        </h1>

                        <p className="mt-3 text-sm text-white/30">
                            Continue into the intelligence layer.
                        </p>
                    </div>

                    {/* Login card */}
                    <form
                        onSubmit={handleLogin}
                        className="
                            relative
                            overflow-hidden
                            rounded-[30px]
                            border
                            border-white/[0.09]
                            bg-white/[0.025]
                            p-6
                            shadow-[inset_0_1px_1px_rgba(255,255,255,0.08),0_30px_100px_rgba(0,0,0,0.25)]
                            backdrop-blur-2xl
                            sm:p-8
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

                        {/* Google */}
                        <button
                            type="button"
                            className="
                                flex
                                w-full
                                items-center
                                justify-center
                                gap-3
                                rounded-2xl
                                border
                                border-white/[0.09]
                                bg-white/[0.045]
                                px-4
                                py-3
                                text-xs
                                font-medium
                                text-white/75
                                transition-all
                                duration-300
                                hover:bg-white/[0.08]
                                hover:text-white
                            "
                        >
                            <span className="text-sm font-semibold">G</span>
                            Continue with Google
                        </button>

                        {/* Divider */}
                        <div className="my-6 flex items-center gap-4">
                            <span className="h-px flex-1 bg-white/[0.07]" />

                            <span className="text-[8px] uppercase tracking-[0.25em] text-white/20">
                                or
                            </span>

                            <span className="h-px flex-1 bg-white/[0.07]" />
                        </div>

                        {/* Email */}
                        <label className="block">
                            <span className="mb-2 block text-[9px] uppercase tracking-[0.2em] text-white/30">
                                Email
                            </span>

                            <input
                                type="email"
                                value={email}
                                onChange={(event) => {
                                    setEmail(event.target.value);
                                    setError("");
                                }}
                                placeholder="you@example.com"
                                autoComplete="email"
                                className="
                                    w-full
                                    rounded-2xl
                                    border
                                    border-white/[0.08]
                                    bg-black/[0.15]
                                    px-4
                                    py-3.5
                                    text-sm
                                    text-white
                                    outline-none
                                    placeholder:text-white/20
                                    transition
                                    focus:border-cyan-300/30
                                    focus:bg-white/[0.035]
                                "
                            />
                        </label>

                        {/* Password */}
                        <label className="mt-5 block">
                            <div className="mb-2 flex items-center justify-between">
                                <span className="text-[9px] uppercase tracking-[0.2em] text-white/30">
                                    Password
                                </span>

                                <button
                                    type="button"
                                    className="
                                        text-[9px]
                                        text-white/20
                                        transition
                                        hover:text-white/50
                                    "
                                >
                                    Forgot?
                                </button>
                            </div>

                            <input
                                type="password"
                                value={password}
                                onChange={(event) => {
                                    setPassword(event.target.value);
                                    setError("");
                                }}
                                placeholder="Your password"
                                autoComplete="current-password"
                                className="
                                    w-full
                                    rounded-2xl
                                    border
                                    border-white/[0.08]
                                    bg-black/[0.15]
                                    px-4
                                    py-3.5
                                    text-sm
                                    text-white
                                    outline-none
                                    placeholder:text-white/20
                                    transition
                                    focus:border-cyan-300/30
                                    focus:bg-white/[0.035]
                                "
                            />
                        </label>

                        {/* Error */}
                        {error && (
                            <motion.p
                                initial={{ opacity: 0, y: -5 }}
                                animate={{ opacity: 1, y: 0 }}
                                className="
                                    mt-4
                                    text-center
                                    text-[10px]
                                    leading-5
                                    text-red-300/70
                                "
                            >
                                {error}
                            </motion.p>
                        )}

                        {/* Login */}
                        <button
                            type="submit"
                            disabled={loading}
                            className="
                                group
                                mt-6
                                flex
                                w-full
                                items-center
                                justify-center
                                gap-2
                                rounded-2xl
                                bg-white
                                px-4
                                py-3.5
                                text-xs
                                font-semibold
                                text-black
                                transition-all
                                duration-300
                                hover:bg-white/90
                                disabled:cursor-not-allowed
                                disabled:opacity-50
                            "
                        >
                            {loading ? "Entering Cognexa..." : "Enter Cognexa"}

                            {!loading && (
                                <ArrowRight
                                    size={14}
                                    className="
                                        transition-transform
                                        duration-300
                                        group-hover:translate-x-1
                                    "
                                />
                            )}
                        </button>

                        {/* Signup */}
                        <p className="mt-6 text-center text-[11px] text-white/25">
                            New to Cognexa?{" "}
                            <button
                                type="button"
                                onClick={() => navigate("/signup")}
                                className="
                                    text-violet-200/70
                                    transition
                                    hover:text-violet-200
                                "
                            >
                                Create an account
                            </button>
                        </p>
                    </form>

                    <p className="mt-7 text-center text-[8px] uppercase tracking-[0.25em] text-white/10">
                        Intelligence begins with understanding
                    </p>

                </motion.div>
            </div>
        </main>
    );
}

export default Login;

