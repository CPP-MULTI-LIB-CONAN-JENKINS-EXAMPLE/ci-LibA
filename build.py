from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    #builder.add_common_builds(pure_c=True, shared_option_name=False)
    builder.add(settings={"build_type": "Debug"}, options={}, env_vars={}, build_requires={})
    builder.add(settings={"build_type": "Release"}, options={}, env_vars={}, build_requires={})
    
    builder.run()    
