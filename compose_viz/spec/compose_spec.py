# generated by datamodel-codegen:
#   filename:  compose-spec.json
#   timestamp: 2023-05-03T07:42:00+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import Extra, Field, conint, constr
from pydantic_yaml import YamlModel, YamlStrEnum


class Cgroup(YamlStrEnum):
    host = "host"
    private = "private"


class CredentialSpec(YamlModel):
    class Config:
        extra = Extra.allow

    config: Optional[str] = None
    file: Optional[str] = None
    registry: Optional[str] = None


class Condition(YamlStrEnum):
    service_started = "service_started"
    service_healthy = "service_healthy"
    service_completed_successfully = "service_completed_successfully"


class DependsOn(YamlModel):
    class Config:
        extra = Extra.allow

    restart: Optional[bool] = None
    condition: Condition


class Extend(YamlModel):
    class Config:
        extra = Extra.allow

    service: str
    file: Optional[str] = None


class Logging(YamlModel):
    class Config:
        extra = Extra.allow

    driver: Optional[str] = None
    options: Optional[Dict[constr(regex=r"^.+$"), Optional[Union[str, float]]]] = None  # type: ignore  # noqa: F722


class Port(YamlModel):
    class Config:
        extra = Extra.allow

    mode: Optional[str] = None
    host_ip: Optional[str] = None
    target: Optional[int] = None
    published: Optional[Union[str, int]] = None
    protocol: Optional[str] = None
    app_protocol: Optional[str] = None # [akaluza] manually added to support OSI-Layer 7


class PullPolicy(YamlStrEnum):
    always = "always"
    never = "never"
    if_not_present = "if_not_present"
    build = "build"
    missing = "missing"


class Ulimit(YamlModel):
    class Config:
        extra = Extra.allow

    hard: int
    soft: int


class Selinux(YamlStrEnum):
    z = "z"
    Z = "Z"


class Bind(YamlModel):
    class Config:
        extra = Extra.allow

    propagation: Optional[str] = None
    create_host_path: Optional[bool] = None
    selinux: Optional[Selinux] = None


class AdditionalVolumeOption(YamlModel):
    class Config:
        extra = Extra.allow

    nocopy: Optional[bool] = None


class Tmpfs(YamlModel):
    class Config:
        extra = Extra.allow

    size: Optional[Union[conint(ge=0), str]] = None  # type: ignore
    mode: Optional[float] = None


class ServiceVolume(YamlModel):
    class Config:
        extra = Extra.allow

    type: str
    source: Optional[str] = None
    target: Optional[str] = None
    read_only: Optional[bool] = None
    consistency: Optional[str] = None
    bind: Optional[Bind] = None
    volume: Optional[AdditionalVolumeOption] = None
    tmpfs: Optional[Tmpfs] = None


class Healthcheck(YamlModel):
    class Config:
        extra = Extra.allow

    disable: Optional[bool] = None
    interval: Optional[str] = None
    retries: Optional[float] = None
    test: Optional[Union[str, List[str]]] = None
    timeout: Optional[str] = None
    start_period: Optional[str] = None


class Order(YamlStrEnum):
    start_first = "start-first"
    stop_first = "stop-first"


class RollbackConfig(YamlModel):
    class Config:
        extra = Extra.allow

    parallelism: Optional[int] = None
    delay: Optional[str] = None
    failure_action: Optional[str] = None
    monitor: Optional[str] = None
    max_failure_ratio: Optional[float] = None
    order: Optional[Order] = None


class ConfigOrder(YamlStrEnum):
    start_first = "start-first"
    stop_first = "stop-first"


class UpdateConfig(YamlModel):
    class Config:
        extra = Extra.allow

    parallelism: Optional[int] = None
    delay: Optional[str] = None
    failure_action: Optional[str] = None
    monitor: Optional[str] = None
    max_failure_ratio: Optional[float] = None
    order: Optional[ConfigOrder] = None


class Limits(YamlModel):
    class Config:
        extra = Extra.allow

    cpus: Optional[Union[float, str]] = None
    memory: Optional[str] = None
    pids: Optional[int] = None


class RestartPolicy(YamlModel):
    class Config:
        extra = Extra.allow

    condition: Optional[str] = None
    delay: Optional[str] = None
    max_attempts: Optional[int] = None
    window: Optional[str] = None


class Preference(YamlModel):
    class Config:
        extra = Extra.allow

    spread: Optional[str] = None


class Placement(YamlModel):
    class Config:
        extra = Extra.allow

    constraints: Optional[List[str]] = None
    preferences: Optional[List[Preference]] = None
    max_replicas_per_node: Optional[int] = None


class DiscreteResourceSpec(YamlModel):
    class Config:
        extra = Extra.allow

    kind: Optional[str] = None
    value: Optional[float] = None


class GenericResource(YamlModel):
    class Config:
        extra = Extra.allow

    discrete_resource_spec: Optional[DiscreteResourceSpec] = None


class GenericResources(YamlModel):
    class Config:
        extra = Extra.allow

    __root__: List[GenericResource]


class ConfigItem(YamlModel):
    class Config:
        extra = Extra.allow

    subnet: Optional[str] = None
    ip_range: Optional[str] = None
    gateway: Optional[str] = None
    aux_addresses: Optional[Dict[constr(regex=r"^.+$"), str]] = None  # type: ignore  # noqa: F722


class Ipam(YamlModel):
    class Config:
        extra = Extra.allow

    driver: Optional[str] = None
    config: Optional[List[ConfigItem]] = None
    options: Optional[Dict[constr(regex=r"^.+$"), str]] = None  # type: ignore  # noqa: F722


class ExternalNetwork(YamlModel):
    class Config:
        extra = Extra.allow

    name: Optional[str] = None


class ExternalVolume(YamlModel):
    class Config:
        extra = Extra.allow

    name: Optional[str] = None


class ExternalSecret(YamlModel):
    name: Optional[str] = None


class ExternalConfig(YamlModel):
    name: Optional[str] = None


class ListOfStrings(YamlModel):
    class Config:
        extra = Extra.allow

    __root__: List[str] = Field(..., unique_items=True)


class ListOrDict(YamlModel):
    class Config:
        extra = Extra.allow

    __root__: Union[
        Dict[constr(regex=r".+"), Optional[Union[str, float, bool]]], List[str]  # type: ignore  # noqa: F722
    ]


class BlkioLimit(YamlModel):
    class Config:
        extra = Extra.allow

    path: Optional[str] = None
    rate: Optional[Union[int, str]] = None


class BlkioWeight(YamlModel):
    class Config:
        extra = Extra.allow

    path: Optional[str] = None
    weight: Optional[int] = None


class ServiceConfigOrSecretItem(YamlModel):
    class Config:
        extra = Extra.allow

    source: Optional[str] = None
    target: Optional[str] = None
    uid: Optional[str] = None
    gid: Optional[str] = None
    mode: Optional[float] = None


class ServiceConfigOrSecret(YamlModel):
    class Config:
        extra = Extra.allow

    __root__: List[Union[str, ServiceConfigOrSecretItem]]


class Constraints(YamlModel):
    class Config:
        extra = Extra.allow

    __root__: Any


class BuildItem(YamlModel):
    class Config:
        extra = Extra.allow

    context: Optional[str] = None
    dockerfile: Optional[str] = None
    dockerfile_inline: Optional[str] = None
    args: Optional[ListOrDict] = None
    ssh: Optional[ListOrDict] = None
    labels: Optional[ListOrDict] = None
    cache_from: Optional[List[str]] = None
    cache_to: Optional[List[str]] = None
    no_cache: Optional[bool] = None
    additional_contexts: Optional[ListOrDict] = None
    network: Optional[str] = None
    pull: Optional[bool] = None
    target: Optional[str] = None
    shm_size: Optional[Union[int, str]] = None
    extra_hosts: Optional[ListOrDict] = None
    isolation: Optional[str] = None
    privileged: Optional[bool] = None
    secrets: Optional[ServiceConfigOrSecret] = None
    tags: Optional[List[str]] = None
    platforms: Optional[List[str]] = None


class BlkioConfig(YamlModel):
    class Config:
        extra = Extra.allow

    device_read_bps: Optional[List[BlkioLimit]] = None
    device_read_iops: Optional[List[BlkioLimit]] = None
    device_write_bps: Optional[List[BlkioLimit]] = None
    device_write_iops: Optional[List[BlkioLimit]] = None
    weight: Optional[int] = None
    weight_device: Optional[List[BlkioWeight]] = None


class ServiceNetwork(YamlModel):
    class Config:
        extra = Extra.allow

    aliases: Optional[ListOfStrings] = None
    ipv4_address: Optional[str] = None
    ipv6_address: Optional[str] = None
    link_local_ips: Optional[ListOfStrings] = None
    priority: Optional[float] = None


class Device(YamlModel):
    class Config:
        extra = Extra.allow

    capabilities: Optional[ListOfStrings] = None
    count: Optional[Union[str, int]] = None
    device_ids: Optional[ListOfStrings] = None
    driver: Optional[str] = None
    options: Optional[ListOrDict] = None


class Devices(YamlModel):
    class Config:
        extra = Extra.allow

    __root__: List[Device]


class Network(YamlModel):
    class Config:
        extra = Extra.allow

    name: Optional[str] = None
    driver: Optional[str] = None
    driver_opts: Optional[Dict[constr(regex=r"^.+$"), Union[str, float]]] = None  # type: ignore  # noqa: F722
    ipam: Optional[Ipam] = None
    external: Optional[bool | ExternalNetwork] = None
    internal: Optional[bool] = None
    enable_ipv6: Optional[bool] = None
    attachable: Optional[bool] = None
    labels: Optional[ListOrDict] = None


class Volume(YamlModel):
    class Config:
        extra = Extra.allow

    name: Optional[str] = None
    driver: Optional[str] = None
    driver_opts: Optional[Dict[constr(regex=r"^.+$"), Union[str, float]]] = None  # type: ignore  # noqa: F722
    external: Optional[ExternalVolume] = None
    labels: Optional[ListOrDict] = None


class Secret(YamlModel):
    class Config:
        extra = Extra.allow

    name: Optional[str] = None
    environment: Optional[str] = None
    file: Optional[str] = None
    external: Optional[ExternalSecret] = None
    labels: Optional[ListOrDict] = None
    driver: Optional[str] = None
    driver_opts: Optional[Dict[constr(regex=r"^.+$"), Union[str, float]]] = None  # type: ignore  # noqa: F722
    template_driver: Optional[str] = None


class Config(YamlModel):
    class Config:
        extra = Extra.allow

    name: Optional[str] = None
    file: Optional[str] = None
    external: Optional[ExternalConfig] = None
    labels: Optional[ListOrDict] = None
    template_driver: Optional[str] = None


class StringOrList(YamlModel):
    class Config:
        extra = Extra.allow

    __root__: Union[str, ListOfStrings]


class Reservations(YamlModel):
    class Config:
        extra = Extra.allow

    cpus: Optional[Union[float, str]] = None
    memory: Optional[str] = None
    generic_resources: Optional[GenericResources] = None
    devices: Optional[Devices] = None


class Resources(YamlModel):
    class Config:
        extra = Extra.allow

    limits: Optional[Limits] = None
    reservations: Optional[Reservations] = None


class Deployment(YamlModel):
    class Config:
        extra = Extra.allow

    mode: Optional[str] = None
    endpoint_mode: Optional[str] = None
    replicas: Optional[int] = None
    labels: Optional[ListOrDict] = None
    rollback_config: Optional[RollbackConfig] = None
    update_config: Optional[UpdateConfig] = None
    resources: Optional[Resources] = None
    restart_policy: Optional[RestartPolicy] = None
    placement: Optional[Placement] = None


class Service(YamlModel):
    class Config:
        extra = Extra.allow

    deploy: Optional[Deployment] = None
    build: Optional[Union[str, BuildItem]] = None
    blkio_config: Optional[BlkioConfig] = None
    cap_add: Optional[List[str]] = Field(None, unique_items=True)
    cap_drop: Optional[List[str]] = Field(None, unique_items=True)
    cgroup: Optional[Cgroup] = None
    cgroup_parent: Optional[str] = None
    command: Optional[Union[str, List[str]]] = None
    configs: Optional[ServiceConfigOrSecret] = None
    container_name: Optional[str] = None
    cpu_count: Optional[conint(ge=0)] = None  # type: ignore
    cpu_percent: Optional[conint(ge=0, le=100)] = None  # type: ignore
    cpu_shares: Optional[Union[float, str]] = None
    cpu_quota: Optional[Union[float, str]] = None
    cpu_period: Optional[Union[float, str]] = None
    cpu_rt_period: Optional[Union[float, str]] = None
    cpu_rt_runtime: Optional[Union[float, str]] = None
    cpus: Optional[Union[float, str]] = None
    cpuset: Optional[str] = None
    credential_spec: Optional[CredentialSpec] = None
    depends_on: Optional[
        Union[ListOfStrings, Dict[constr(regex=r"^[a-zA-Z0-9._-]+$"), DependsOn]]  # type: ignore  # noqa: F722, E501
    ] = None
    device_cgroup_rules: Optional[ListOfStrings] = None
    devices: Optional[List[str]] = Field(None, unique_items=True)
    dns: Optional[StringOrList] = None
    dns_opt: Optional[List[str]] = Field(None, unique_items=True)
    dns_search: Optional[StringOrList] = None
    domainname: Optional[str] = None
    entrypoint: Optional[Union[str, List[str]]] = None
    env_file: Optional[StringOrList] = None
    environment: Optional[ListOrDict] = None
    expose: Optional[List[Union[str, float]]] = Field(None, unique_items=True)
    extends: Optional[Union[str, Extend]] = None
    external_links: Optional[List[str]] = Field(None, unique_items=True)
    extra_hosts: Optional[ListOrDict] = None
    group_add: Optional[List[Union[str, float]]] = Field(None, unique_items=True)
    healthcheck: Optional[Healthcheck] = None
    hostname: Optional[str] = None
    image: Optional[str] = None
    init: Optional[bool] = None
    ipc: Optional[str] = None
    isolation: Optional[str] = None
    labels: Optional[ListOrDict] = None
    links: Optional[List[str]] = Field(None, unique_items=True)
    logging: Optional[Logging] = None
    mac_address: Optional[str] = None
    mem_limit: Optional[Union[float, str]] = None
    mem_reservation: Optional[Union[str, int]] = None
    mem_swappiness: Optional[int] = None
    memswap_limit: Optional[Union[float, str]] = None
    network_mode: Optional[str] = None
    networks: Optional[
        Union[
            ListOfStrings, Dict[constr(regex=r"^[a-zA-Z0-9._-]+$"), Optional[ServiceNetwork]]  # type: ignore  # noqa: F722, E501
        ]
    ] = None
    oom_kill_disable: Optional[bool] = None
    oom_score_adj: Optional[conint(ge=-1000, le=1000)] = None  # type: ignore
    pid: Optional[str] = None
    pids_limit: Optional[Union[float, str]] = None
    platform: Optional[str] = None
    ports: Optional[List[Union[float, str, Port]]] = Field(None, unique_items=True)
    privileged: Optional[bool] = None
    profiles: Optional[ListOfStrings] = None
    pull_policy: Optional[PullPolicy] = None
    read_only: Optional[bool] = None
    restart: Optional[str] = None
    runtime: Optional[str] = None
    scale: Optional[int] = None
    security_opt: Optional[List[str]] = Field(None, unique_items=True)
    shm_size: Optional[Union[float, str]] = None
    secrets: Optional[ServiceConfigOrSecret] = None
    sysctls: Optional[ListOrDict] = None
    stdin_open: Optional[bool] = None
    stop_grace_period: Optional[str] = None
    stop_signal: Optional[str] = None
    storage_opt: Optional[Dict[str, Any]] = None
    tmpfs: Optional[StringOrList] = None
    tty: Optional[bool] = None
    ulimits: Optional[Dict[constr(regex=r"^[a-z]+$"), Union[int, Ulimit]]] = None  # type: ignore  # noqa: F722
    user: Optional[str] = None
    uts: Optional[str] = None
    userns_mode: Optional[str] = None
    volumes: Optional[List[Union[str, ServiceVolume]]] = Field(None, unique_items=True)
    volumes_from: Optional[List[str]] = Field(None, unique_items=True)
    working_dir: Optional[str] = None


class ComposeSpecification(YamlModel):
    class Config:
        extra = Extra.allow

    version: Optional[str] = Field(None, description="declared for backward compatibility, ignored.")
    name: Optional[constr(regex=r"^[a-z0-9][a-z0-9_-]*$")] = Field(  # type: ignore  # noqa: F722
        None,
        description="define the Compose project name, until user defines one explicitly.",
    )
    services: Optional[Dict[constr(regex=r"^[a-zA-Z0-9._-]+$"), Service]] = None  # type: ignore  # noqa: F722
    networks: Optional[Dict[constr(regex=r"^[a-zA-Z0-9._-]+$"), Optional[Network]]] = None  # type: ignore  # noqa: F722
    volumes: Optional[Dict[constr(regex=r"^[a-zA-Z0-9._-]+$"), Optional[Volume]]] = None  # type: ignore  # noqa: F722
    secrets: Optional[Dict[constr(regex=r"^[a-zA-Z0-9._-]+$"), Secret]] = None  # type: ignore  # noqa: F722
    configs: Optional[Dict[constr(regex=r"^[a-zA-Z0-9._-]+$"), Config]] = None  # type: ignore  # noqa: F722
